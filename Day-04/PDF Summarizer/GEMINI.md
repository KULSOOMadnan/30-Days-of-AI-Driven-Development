# Project: PDF Summarizer & Quiz Generator
**Role:** Senior Python AI Engineer

---

## 1. Objective

Build a fully modular **PDF Summarizer & Quiz Generator** using:

- **Gemini-CLI** (spec-driven development)
- **openai-agents SDK** (NOT the standard openai library)
- **PyPDF** for extraction
- **Streamlit UI**
- **Context07 MCP** (for scaffolding ONLY)

The final system must read PDFs, extract text, summarize content, generate quizzes, and display output through a clean Streamlit interface with JSON-based history.

---

## 2. Critical Technical Constraints (STRICT)

### 2.1 Zero-Bloat Protocol (CRITICAL)

You MUST follow these rules:

- ❌ Do NOT add extra code.
- ❌ Do NOT guess agent syntax.
- ❌ Do NOT create abstractions beyond what is described.
- ❌ Do NOT generate comments unless explicitly stated.
- ✅ Only implement exactly what this spec asks for.

### 2.2 SDK Configuration Rules

You MUST use:

- **openai-agents SDK**  
  (NOT openai, NOT openai.OpenAI, NOT openai.chat, NOT langchain)

- **Model initialization via:**
```python
  OpenaiChatCompletionModel(model="gemini-2.0-flash")
```

- **Base URL:**
```
  https://generativelanguage.googleapis.com/v1beta/openai/
```

- **Environment variable:**
```
  GEMINI_API_KEY
```

❗ **If ANY ImportError, SyntaxError, or attribute error occurs → STOP.**  
You MUST call `get-library-docs` through Context07 before proceeding.

### 2.3 Context07 MCP Requirement

Context07 MCP is required **ONLY at scaffolding time** to:

- Load real SDK documentation
- View decorators, class definitions, parameters
- Prevent SDK hallucinations
- Force correct agent/tool syntax

**NOT used inside Python during runtime.**

### 2.4 Dependency Rules

Use **uv** for environment creation and dependency installation.

**Only install:**
- `openai-agents`
- `streamlit`
- `pypdf`
- `python-dotenv`

if need in project can do more **DO NOT INSTALL IF ALREADY INSTALL** 

---

## 3. Architecture & Folder Structure

(Current working directory is project root.)
```
.
├── .env
├── GEMINI.md                 # <-- this file
├── agent/
│   ├── GEMINI.md
│   ├── agent.py
│   └── tools.py
├── core/
│   ├── GEMINI.md
│   ├── pdf_reader.py
│   ├── summarizer.py
│   └── quiz_generator.py
├── ui/
│   ├── GEMINI.md
│   ├── app.py
│   └── components/
│       ├── uploader.py
│       ├── summary_viewer.py
│       ├── quiz_viewer.py
│       └── history_viewer.py
├── storage/
│   ├── GEMINI.md
│   └── history.json
├── screenshots/
│   └── gemini_prompt.png
├── pyproject.toml
└── README.md
```

---

## 4. Implementation Steps (STRICT ORDER)

### Step 1 — SDK Verification (MANDATORY)

**Before writing ANY code:**

Use Context07 MCP tool:
```
get-library-docs("openai-agents")
```

**Check:**
- tool decorator format
- Agent class initialization
- Model configuration format
- How to attach tools
- Required params in constructors

**If anything is unclear → repeat docs call.**

---

### Step 2 — PDF Tools (agent/tools.py)

Implement EXACTLY these 3 tools:

#### 1. `extract_pdf_text(file_path: str)`
- Use PyPDF
- Multi-page extraction
- Return string

#### 2. `summarize_text(text: str, summary_type: str)`
- Will be invoked by the agent
- `summary_type` options:
  - `"short"`
  - `"medium"`
  - `"detailed"`

#### 3. `generate_quiz(text: str)`
- Create MCQs and mixed questions
- Base ONLY on raw PDF text (not summary)

Tools must be implemented using the **exact syntax from openai-agents docs** (decorator or FunctionTool).

---

### Step 3 — Agent Setup (agent/agent.py)

The agent must:

**Initialize:**
```python
OpenaiChatCompletionModel("gemini-2.0-flash")
```

**Bind tools from tools.py**



**Use a single system prompt:**
```
You are a PDF Summarizer & Quiz Generator.
Always base your output strictly on the extracted PDF text.
```

- ❌ NO streaming.
- ❌ NO advanced memory.
- ❌ NO conversation context persistence.

---

### Step 4 — Core Logic (core/)

#### `pdf_reader.py`
- Thin wrapper around PyPDF
- No extra formatting

#### `summarizer.py`
- Calls the agent using `summarize_text` tool

#### `quiz_generator.py`
- Calls the agent using `generate_quiz` tool

**Minimal logic — Zero-Bloat applies.**

---

### Step 5 — Streamlit UI (ui/app.py)

**UI must include:**
- Upload Page
- Summary Page
- Quiz Page
- History Page


## G. Streamlit UI

* Sidebar navigation:

  * Upload
  * Summary
  * Quiz
  * History
* Modular components in `ui/components/`
* Clean layout, responsive design
* Prefer Poppins or Inter fonts

**Using these components:**
- `uploader.py`
- `summary_viewer.py`
- `quiz_viewer.py`
- `history_viewer.py`

**Design:**
- Fonts: Inter or Poppins
- Style: simple, responsive, clean
- ❌ No animations, no fancy CSS, no extras.

---

### Step 6 — JSON Storage (storage/history.json)

**Each entry must include:**
- `filename`
- `summary_type`
- `summary`
- `quiz`
- `timestamp`

**History file must be auto-created if missing.**

---

### Step 7 — Screenshot Requirement

Save the Gemini-CLI prompt as:
```
/screenshots/gemini_prompt.png
```

---

## 5. Testing Scenarios

### 1. Summarization Flow
- Upload → Extract → Summarize → Display

### 2. Quiz Flow
- Generate quiz → Display MCQs + mixed questions

### 3. History
- Captured accurately in JSON

### 4. Invalid File
- Upload JPG → return simple error

### 5. Large File
- Multi-page PDF works without crashing