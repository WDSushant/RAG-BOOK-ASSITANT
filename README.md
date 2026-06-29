# 📚 RAG Book Assistant using Gemini & LangChain

An AI-powered **Retrieval-Augmented Generation (RAG)** application built with **Streamlit**, **Google Gemini**, **LangChain**, and **ChromaDB**.

Upload any PDF book or document and ask natural language questions. The assistant retrieves the most relevant sections from the document and generates accurate answers using Google's Gemini model.

---

## 🚀 Features

* 📄 Upload any PDF document
* ✂️ Automatic text chunking
* 🔍 Semantic search using Gemini Embeddings
* 🗄️ Persistent Chroma Vector Database
* 🤖 Question Answering with Gemini 2.5 Flash
* ⚡ Fast document retrieval
* 🎯 Context-aware responses
* 💻 Simple Streamlit interface

---

## 🛠️ Tech Stack

| Technology    | Purpose               |
| ------------- | --------------------- |
| Python        | Programming Language  |
| Streamlit     | Frontend UI           |
| LangChain     | LLM Orchestration     |
| Google Gemini | LLM & Embeddings      |
| ChromaDB      | Vector Database       |
| PyPDF         | PDF Loading           |
| python-dotenv | Environment Variables |

---

## 📂 Project Structure

```
RAG-Book-Assistant/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── chroma_db/
```

> **Note:** The `chroma_db/` folder is generated automatically after processing a PDF and should not be committed to GitHub.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/RAG-Book-Assistant.git
cd RAG-Book-Assistant
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

You can obtain a Gemini API key from Google AI Studio.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 📖 How It Works

1. Upload a PDF document.
2. The PDF is loaded using PyPDF.
3. The text is split into smaller chunks.
4. Gemini Embeddings convert each chunk into vectors.
5. ChromaDB stores the vectors locally.
6. When a question is asked:

   * Relevant chunks are retrieved.
   * Gemini 2.5 Flash receives the retrieved context.
   * The model generates an answer based only on the document.

---

## 📸 Demo

1. Upload a PDF.
2. Click **Create Vector Database**.
3. Ask any question about the document.
4. View the generated answer and retrieved context.

---

## 📚 Future Improvements

* Chat history
* Multiple PDF support
* Source citations
* Hybrid Search (BM25 + Vector Search)
* Conversation Memory
* Reranking
* Metadata filtering
* PDF summarization
* Deploy on Streamlit Community Cloud
* Docker support

---

## 📋 Requirements

* Python 3.10+
* Google Gemini API Key
* Internet connection

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sushant Solanki**

If you found this project useful, consider giving it a ⭐ on GitHub.
