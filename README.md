# 🎯 AI Job Application Assistant

An intelligent, AI-powered job application assistant built with GenAI + Agentic AI patterns.

**Perfect for:** Fresher AI engineer portfolios | Interview demonstrations | Personal job search

---

## 🏗️ Architecture Overview

```
User uploads resume
        │
        ▼
┌─────────────────────┐
│  Agent 1: Resume    │  ← pdfplumber / python-docx + Groq LLaMA3
│  Analysis Agent     │    Extracts skills, detects domain
└────────┬────────────┘
         │ profile dict
         ▼
┌─────────────────────┐
│  Agent 2: Job       │  ← RemoteOK + Arbeitnow + Adzuna APIs
│  Search Agent       │    Fetches real matching jobs
└────────┬────────────┘
         │ jobs list
         ▼
┌─────────────────────┐
│  Agent 3: Matching  │  ← sentence-transformers (MiniLM)
│  Agent              │    Cosine similarity scoring
└────────┬────────────┘
         │ ranked jobs
         ▼
┌─────────────────────┐
│  Agent 4: Resume    │  ← Groq LLaMA3
│  Optimizer Agent    │    ATS-friendly resume generation
└────────┬────────────┘
         │ optimized resume
         ▼
┌─────────────────────┐
│  Agent 5: Outreach  │  ← Groq LLaMA3
│  Agent              │    Cover letter + Email + LinkedIn
└─────────────────────┘
         │
         ▼
   SQLite Tracker
```

## 🛠️ Tech Stack

| Layer | Tech | Why |
|-------|------|-----|
| Frontend | Streamlit | Fast, Python-native dashboards |
| GenAI | Groq (LLaMA3-8B) | Free, fast inference |
| Embeddings | sentence-transformers | Local semantic matching |
| Resume Parse | pdfplumber + python-docx | Reliable PDF/DOCX extraction |
| Job APIs | RemoteOK, Arbeitnow, Adzuna | Free, no-auth required |
| Database | SQLite | Simple, file-based, no server |
| NLP | spaCy + regex | Skill extraction |

---

## 🚀 Setup & Installation

### Step 1: Clone / Extract Project
```bash
cd job_assistant
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### Step 5: Configure Environment
```bash
cp .env .env.local
# Edit .env and add your API keys
```

Required:
- `GROQ_API_KEY` → Get free at https://console.groq.com

Optional (for more jobs):
- `ADZUNA_APP_ID` + `ADZUNA_APP_KEY` → Get free at https://developer.adzuna.com

### Step 6: Run the App
```bash
streamlit run app.py
```

Open: http://localhost:8501

---

## 📁 Project Structure

```
job_assistant/
│
├── app.py                          # Main Streamlit entry point + home page
├── requirements.txt                # All dependencies
├── .env                            # API keys (never commit this!)
├── README.md                       # This file
│
├── agents/                         # The 5 AI agents
│   ├── resume_agent.py             # Agent 1: Parse + analyze resume
│   ├── jobs_agent.py               # Agent 2: Fetch real jobs
│   ├── matching_agent.py           # Agent 3: Semantic similarity scoring
│   ├── resume_optimizer_agent.py   # Agent 4: ATS resume generation
│   └── outreach_agent.py           # Agent 5: Cover letter, email, LinkedIn
│
├── utils/                          # Shared utilities
│   ├── parser.py                   # PDF/DOCX text extraction
│   ├── embeddings.py               # sentence-transformers wrapper
│   ├── database.py                 # SQLite CRUD operations
│   └── api_client.py               # RemoteOK/Arbeitnow/Adzuna API clients
│
├── pages/                          # Streamlit multipage pages
│   ├── 1_Upload.py                 # Resume upload page
│   ├── 2_Profile.py                # Extracted profile viewer
│   ├── 3_Jobs.py                   # Job search + match scores
│   ├── 4_Resume_Optimizer.py       # ATS resume generator
│   ├── 5_Outreach.py               # Recruiter messages
│   └── 6_Tracker.py                # Application tracker
│
├── database/                       # SQLite DB files (auto-created)
├── resumes/                        # Uploaded resume files
└── generated/                      # Generated DOCX resumes
```

---

## 🎯 How Each Agent Works

### Agent 1: Resume Analysis Agent (`agents/resume_agent.py`)
- Sends resume text to Groq LLaMA3 with a structured JSON extraction prompt
- Falls back to regex/keyword matching if Groq fails
- Runs rule-based domain detection (14 domains supported)
- **Interview talking point:** "I used a hybrid approach — LLM for semantic extraction, rules for reliability"

### Agent 2: Job Search Agent (`agents/jobs_agent.py`)
- Maps detected domain to optimized search queries
- Calls 3 APIs: RemoteOK (no key), Arbeitnow (no key), Adzuna (optional key)
- Deduplicates by title+company across sources
- **Interview talking point:** "API aggregation with deduplication — classic data pipeline pattern"

### Agent 3: Matching Agent (`agents/matching_agent.py`)
- Converts resume + job descriptions to 384-dim embedding vectors
- Uses batch cosine similarity for efficiency (all jobs in one model call)
- Overlays keyword-based skill gap analysis
- **Interview talking point:** "Semantic matching vs keyword matching — embeddings capture meaning, not just words"

### Agent 4: Resume Optimizer Agent (`agents/resume_optimizer_agent.py`)
- Strict prompt: NEVER fabricate experience
- Rewrites bullets with action verbs and JD keywords
- Exports ATS-safe DOCX (no tables, no text boxes)
- **Interview talking point:** "Prompt engineering for safety — hallucination prevention in production systems"

### Agent 5: Outreach Agent (`agents/outreach_agent.py`)
- Generates 3 different content types with different prompts
- LinkedIn message strictly under 280 characters
- **Interview talking point:** "Output format constraints in LLM prompting"

---

## 🔑 API Keys Guide

| API | Key Required | Get It | Free Tier |
|-----|-------------|--------|-----------|
| Groq | ✅ Yes | https://console.groq.com | Yes — generous |
| RemoteOK | ❌ No | Public API | Always free |
| Arbeitnow | ❌ No | Public API | Always free |
| Adzuna | ⚡ Optional | https://developer.adzuna.com | Yes |

---

## 🤔 Interview Questions & Answers

**Q: What is agentic AI?**
A: AI systems where multiple models/components work together in a pipeline, each with a specific role. Here, 5 agents handle different tasks — parsing, searching, matching, optimizing, generating.

**Q: Why sentence-transformers over OpenAI embeddings?**
A: sentence-transformers runs locally, is free, and 'all-MiniLM-L6-v2' is fast enough for real-time matching. For production at scale, I'd switch to a managed embedding API.

**Q: How did you prevent hallucination in the Resume Optimizer?**
A: Explicit prompt constraints: "Extract ONLY what is written. Do NOT invent." + returning original data as fallback if the LLM output fails JSON parsing.

**Q: Why SQLite and not PostgreSQL?**
A: Right tool for right job. SQLite is perfect for single-user, local applications. No server to manage, no credentials to configure. For multi-user production, I'd migrate to PostgreSQL.

**Q: What would you improve with more time?**
A: (1) Add vector search with pgvector for faster matching at scale, (2) Add a feedback loop where user ratings improve matching, (3) Add more job sources via SerpAPI, (4) Add email sending via SendGrid.

---

## 📝 License

Personal portfolio project. Free to use and modify.
