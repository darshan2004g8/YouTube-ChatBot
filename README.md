# 🎥 YouTube Chatbot

An intelligent Generative AI-powered YouTube Chatbot that allows users to interact with any YouTube video using natural language. The application extracts the video's English transcript, converts it into vector embeddings, stores them in FAISS, and uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses.
Built with Streamlit, LangChain, Google Gemini API or OpenAI API, YouTube Transcript API, Embeddings, and FAISS.

**🚀 Features**
📺 Retrieve English transcripts from YouTube videos
💬 Ask questions about video content
📝 Generate concise or detailed summaries
🎯 Context-aware answers using Retrieval-Augmented Generation (RAG)
⚡ Fast semantic search using FAISS Vector Store
🤖 Supports both Google Gemini API and OpenAI API
🌐 Simple and interactive Streamlit web interface
📚 Semantic document retrieval with embeddings
🔍 Accurate answers based only on the video transcript

#[**🏗️ System Architecture**]
                YouTube Video URL / Video ID
                           │
                           ▼
               YouTube Transcript API
                           │
                           ▼
                  Transcript Extraction
                           │
                           ▼
                  Text Chunking (LangChain)
                           │
                           ▼
                    Embedding Generation
               (Gemini / OpenAI Embeddings)
                           │
                           ▼
                  FAISS Vector Database
                           │
                           ▼
                  Similarity Search (RAG)
                           │
                           ▼
            Gemini API / OpenAI LLM Response
                           │
                           ▼
                  Streamlit User Interface


**💡 How It Works**
1. Enter a YouTube Video URL or Video ID.
2. The application retrieves the English transcript.
3. The transcript is split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored inside the FAISS vector database.
6. User queries are converted into embeddings.
7. Similar transcript chunks are retrieved using semantic search.
8. Retrieved context is passed to the LLM (Gemini/OpenAI).
9. The chatbot generates an accurate context-based response.

**📷 Application Workflow**
Input YouTube URL
        │
        ▼
Retrieve Transcript
        │
        ▼
Chunk Transcript
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
        ▼
User Question
        │
        ▼
Semantic Retrieval
        │
        ▼
LLM (Gemini/OpenAI)
        │
        ▼
Generated Response

**🎯 Example Questions**
1. Summarize this video.
2. What are the key points discussed?
3. Explain the main concept in simple terms.
4. What are the advantages mentioned?
5. Give me important interview questions from this video.
6. What examples are provided?
7. Explain the conclusion.
8. List the important topics covered.
9. Generate revision notes.

**🤝 Contributing**

Contributions are welcome!

**📄 License**

This project is licensed under the MIT License. Feel free to use, modify, and distribute it in accordance with the license terms.

**👨‍💻 Author**

Darshan T V

AI/ML Engineer | Generative AI Developer
