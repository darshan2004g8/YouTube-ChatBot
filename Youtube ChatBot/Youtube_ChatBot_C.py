#pip install -q streamlit youtube-transcript-api langchain langchain-openai faiss-cpu

import os 
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.title("YouTube Chatbot (OpenAI)")

# User inputs
youtube_url = st.text_input("Enter YouTube URL:")
query = st.text_input("Ask a question about the video:")

if youtube_url:
    try:
        video_id = youtube_url.split("v=")[-1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([item['text'] for item in transcript_list])

        # Text Splitting
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = text_splitter.create_documents([transcript_text])

        # Embeddings & Vector Store (using OpenAI embeddings)
        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        vectorstore = FAISS.from_documents(docs, embeddings)

        # RAG Chain using LCEL (using OpenAI chat model)
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
        prompt = ChatPromptTemplate.from_template(template)

        rag_chain = (
            {"context": vectorstore.as_retriever(), "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )

        if query:
            response = rag_chain.invoke(query)
            st.write("### Answer:")
            st.write(response)

    except Exception as e:
        st.error(f"Error: {e}")