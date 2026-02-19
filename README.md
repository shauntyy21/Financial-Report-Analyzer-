# Financial Report Analyzer 📊

A fully local, privacy-first **PDF Question Answering system** built for financial document analysis. Upload annual reports, earnings PDFs, or any financial document and ask detailed questions — all processing happens on your machine using Ollama.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-orange)

---

## ✨ Features

- 📤 **Upload PDFs** directly through the web UI
- 🧠 **RAG Pipeline** — Retrieval-Augmented Generation for accurate, context-grounded answers
- 💾 **Embedding Cache** — PDFs are embedded once and cached as FAISS indexes for fast re-queries
- 🔒 **100% Local** — No data leaves your machine; no API keys required
- 💬 **Detailed Answers** — Prompts are engineered for precise financial data extraction

---

## 🏗️ Architecture

```
User uploads PDF
      │
      ▼
 PyPDF2 extracts text
      │
      ▼
 RecursiveCharacterTextSplitter
 chunks text (1000 chars, 50 overlap)
      │
      ▼
 OllamaEmbeddings (nomic-embed-text)
 converts chunks → vectors
      │
      ▼
 FAISS Vector Store
 saved to /embeddings/<md5hash>.faiss
      │
      ▼
 similarity_search(query, k=2)
 retrieves top relevant chunks
      │
      ▼
 Ollama LLM (gemma3:1b)
 generates detailed answer
      │
      ▼
 Streamlit UI displays response
```

---

## � Project Structure

```
Financial-Report-Analyzer/
│
├── app.py               # Streamlit web UI
├── rag.py               # Core RAG pipeline (DocumentProcessor, RAGSystem)
├── requirements.txt     # Python dependencies
├── .gitignore
│
├── knowledge_base/      # ← Drop your PDFs here (git-ignored)
└── embeddings/          # ← Auto-generated FAISS cache (git-ignored)
```

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+**
2. **[Ollama](https://ollama.ai/)** — install and make sure it's running

### 1. Clone the repo

```bash
git clone https://github.com/shauntyy21/Financial-Report-Analyzer-.git
cd Financial-Report-Analyzer-
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull the required Ollama models

```bash
ollama pull nomic-embed-text   # embedding model
ollama pull gemma3:1b          # LLM for answering
```

### 5. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖥️ Usage

1. **Upload a PDF** using the sidebar file uploader (e.g. a quarterly earnings report)
2. **Type your question** in the text area, e.g.:
   - *"What is the Operating Cash Flow to PAT percentage?"*
   - *"What was the sequential revenue growth over the last 4 quarters?"*
   - *"Summarize the key financial highlights for Q3."*
3. **Click "Get Answer"** — the system retrieves relevant passages and generates a detailed response

---

## ⚙️ Configuration

All parameters are in the `RAGConfig` dataclass inside `rag.py`:

| Parameter | Default | Description |
|---|---|---|
| `embedding_model` | `nomic-embed-text` | Ollama model used for embeddings |
| `llm_model` | `gemma3:1b` | Ollama LLM used for answer generation |
| `chunk_size` | `1000` | Characters per text chunk |
| `chunk_overlap` | `50` | Overlap between adjacent chunks |
| `top_k` | `2` | Number of chunks retrieved per query |
| `batch_size` | `10` | Chunks processed per embedding batch |

To use a more capable model (e.g. for better answers):

```python
llm_model: str = "llama3"   # or "mistral", "phi3", etc.
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI |
| `langchain` | RAG orchestration |
| `langchain-community` | Ollama + FAISS integrations |
| `langchain-text-splitters` | Document chunking |
| `faiss-cpu` | Vector similarity search |
| `PyPDF2` | PDF text extraction |
| `ollama` | Local LLM inference |

---

## ⚠️ Notes

- **First query on a new PDF** takes longer — it processes and embeds the document
- Subsequent queries on the same PDF are fast (uses cached FAISS index)
- PDFs must be **text-based** (scanned image PDFs won't work without OCR)
- Embedding cache is stored in `embeddings/` — delete it to force re-processing

---

## � Troubleshooting

| Problem | Fix |
|---|---|
| `Connection refused` on query | Make sure Ollama is running (`ollama serve`) |
| `No PDF files found` | Upload a PDF via the sidebar first |
| Slow first response | Normal — PDF is being embedded for the first time |
| Poor answer quality | Try a larger model: `ollama pull llama3` and update `llm_model` in `rag.py` |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push and open a PR
