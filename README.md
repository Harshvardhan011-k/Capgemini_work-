# 🧠 AI Research Assistant

A complete AI-powered research assistant built for a final-year college project. It searches the web, scrapes content, processes it with NLP, stores it in a vector database, and generates detailed research reports using an LLM.

## 📁 Project Structure

```
Research_model/
├── backend/
│   ├── data/
│   │   ├── users.json          # User credentials
│   │   ├── reports.json        # Saved research reports
│   │   └── chroma_db/          # ChromaDB vector store (auto-created)
│   ├── main.py                 # FastAPI app + all endpoints
│   ├── config.py               # Configuration and constants
│   ├── storage.py              # JSON file operations
│   ├── nlp_processor.py        # NLTK, spaCy, KeyBERT pipeline
│   ├── vector_store.py         # ChromaDB + SentenceTransformers
│   ├── searcher.py             # Tavily search + Trafilatura scraping
│   ├── report_generator.py     # OpenRouter LLM integration
│   ├── requirements.txt
│   └── .env                    # API keys (fill this in!)
├── frontend/
│   ├── index.html              # Login page
│   ├── pages/
│   │   ├── dashboard.html      # Stats & overview
│   │   ├── research.html       # New research + progress tracker
│   │   ├── report.html         # Full report viewer + chat
│   │   └── history.html        # Research history
│   ├── components/
│   │   └── app.js              # Shared JS: auth, API, helpers
│   └── styles/
│       └── main.css            # Complete responsive CSS
├── setup.bat                   # One-click setup
├── start.bat                   # Start the server
└── README.md
```

## ⚙️ Prerequisites

- **Python 3.10+** installed and in PATH
- **Tavily API key** → https://tavily.com (free tier available)
- **OpenRouter API key** → https://openrouter.ai (free tier available)

## 🚀 Quick Start

### Step 1: Add API Keys
Edit `backend/.env`:
```env
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxx
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxx
```

### Step 2: Run Setup (first time only)
```bat
setup.bat
```
This installs all Python packages, the spaCy model, and NLTK data.

### Step 3: Start the Server
```bat
start.bat
```

### Step 4: Open the App
Open `frontend/index.html` directly in your browser.

**Default credentials:**
- Username: `admin` / Password: `admin123`
- Username: `student` / Password: `student123`

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/login` | Authenticate user |
| POST | `/api/research/stream` | Start research (SSE stream) |
| GET | `/api/reports` | List all reports |
| GET | `/api/reports/{id}` | Get single report |
| DELETE | `/api/reports/{id}` | Delete report |
| POST | `/api/chat` | Chat with a report (RAG) |
| GET | `/api/stats` | Research statistics |

**Interactive API docs:** http://localhost:8000/docs

## 🔄 Research Workflow

```
User Input (topic + depth + recency)
        ↓
1. Tavily API → Web Search Results
        ↓
2. Trafilatura → Scrape Article Text
        ↓
3. NLTK → Tokenize, Remove Stopwords, Lemmatize
   spaCy → Named Entity Recognition
   KeyBERT → Keyword Extraction
        ↓
4. Sentence Transformers → Generate Embeddings
        ↓
5. ChromaDB → Store Vectors
        ↓
6. ChromaDB → RAG Retrieval (top-k chunks)
        ↓
7. OpenRouter (Mistral-7B) → Generate Report
        ↓
8. reports.json → Save Report
        ↓
Frontend → Display Results
```

## 📊 Data Schemas

### users.json
```json
{
  "users": [{
    "id": "u1",
    "username": "admin",
    "password": "admin123",
    "name": "Admin User",
    "created_at": "2024-01-01T00:00:00"
  }]
}
```

### reports.json
```json
{
  "reports": [{
    "id": "uuid",
    "user_id": "u1",
    "username": "admin",
    "topic": "Quantum Computing",
    "depth": "Medium",
    "recency": "6 Months",
    "report": "## Executive Summary...",
    "keywords": [{"word": "quantum", "score": 0.85}],
    "entities": [{"text": "IBM", "label": "ORG"}],
    "sources": [{"url": "...", "title": "..."}],
    "session_id": "uuid",
    "word_count": 1200,
    "created_at": "2024-01-01T12:00:00"
  }]
}
```

## 🎛️ Configuration

Edit `backend/config.py` to change:
- `OPENROUTER_MODEL` – default: `mistralai/mistral-7b-instruct`
- `DEPTH_CONFIG` – number of sources per depth level
- `RECENCY_DAYS` – date range for each recency option
- `EMBEDDING_MODEL` – default: `all-MiniLM-L6-v2`

## 🌟 Features

- **🔐 Login System** – username/password auth with JSON storage
- **🌐 Web Research** – Tavily API searches with recency filtering
- **📥 Content Scraping** – Trafilatura extracts clean article text
- **🧬 NLP Pipeline** – tokenization, stopwords, lemmatization, NER, keyword extraction
- **🔢 Vector Embeddings** – Sentence Transformers (all-MiniLM-L6-v2)
- **🗃️ Vector Storage** – Persistent ChromaDB with semantic search
- **🎯 RAG** – Retrieval Augmented Generation for accurate reports
- **✍️ AI Reports** – Structured markdown reports via OpenRouter LLM
- **💬 Chat Interface** – Ask questions about any report using RAG
- **☁️ Keyword Cloud** – Visual keyword frequency display
- **🏷️ Named Entities** – Color-coded entity type display
- **🔗 Source Viewer** – All scraped sources with links
- **📊 Statistics** – Report counts, depth distribution, keyword trends
- **📚 History** – Searchable, filterable report archive
- **📱 Responsive** – Works on desktop and mobile

## 🛠️ Troubleshooting

**spaCy model not found:**
```bash
python -m spacy download en_core_web_sm
```

**CORS errors:** Ensure the backend is running on port 8000 before opening the frontend.

**Slow first run:** Sentence Transformer model downloads on first use (~90MB).

**API key errors:** Double-check `.env` file has no spaces around `=`.
