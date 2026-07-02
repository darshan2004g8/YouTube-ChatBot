#pip install -q streamlit youtube-transcript-api langchain langchain-google-genai faiss-cpu

import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

import streamlit as st
import os
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.title("│ YouTube Chatbot")

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

        # Embeddings & Vector Store
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
        vectorstore = FAISS.from_documents(docs, embeddings)

        # RAG Chain using LCEL
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

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