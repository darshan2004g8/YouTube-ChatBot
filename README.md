<h2>🎥 Generative AI YouTube Chatbot</h2>

An intelligent Generative AI-powered YouTube Chatbot that allows users to interact with any YouTube video using natural language. The application extracts the video's English transcript, converts it into vector embeddings, stores them in FAISS, and uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses.
Built with Streamlit, LangChain, Google Gemini API or OpenAI API, YouTube Transcript API, Embeddings, and FAISS.

<h2>🚀 Features</h2>

1. Retrieve English transcripts from YouTube videos
2. Ask questions about video content
3. Generate concise or detailed summaries
4. Context-aware answers using Retrieval-Augmented Generation (RAG)
5. Fast semantic search using FAISS Vector Store
6. Supports both Google Gemini API and OpenAI API
7. Simple and interactive Streamlit web interface
8. Semantic document retrieval with embeddings
9. Accurate answers based only on the video transcript

<h2>🏗️ System Architecture</h2>
  
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


<h2>💡 How It Works</h2>
1. Enter a YouTube Video URL or Video ID.
2. The application retrieves the English transcript.
3. The transcript is split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored inside the FAISS vector database.
6. User queries are converted into embeddings.
7. Similar transcript chunks are retrieved using semantic search.
8. Retrieved context is passed to the LLM (Gemini/OpenAI).
9. The chatbot generates an accurate context-based response.

<h2>📷 Application Workflow</h2>

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


<h2>🎯 Example Question</h2>
1. Summarize this video.
2. What are the key points discussed?
3. Explain the main concept in simple terms.
4. What are the advantages mentioned?
5. Give me important interview questions from this video.
6. What examples are provided?
7. Explain the conclusion.
8. List the important topics covered.
9. Generate revision notes.

<h2>🤝 Contributing</h2>

Contributions are welcome!

<h2>📄 License</h2>

This project is licensed under the MIT License. Feel free to use, modify, and distribute it in accordance with the license terms.

<h2>👨‍💻 Author</h2>

**Darshan T V**

AI/ML Engineer | Generative AI Developer
