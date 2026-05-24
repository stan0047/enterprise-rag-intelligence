<div align="center">

# 🧠 Enterprise RAG Intelligence

**Production-grade Retrieval-Augmented Generation with Role-Based Access Control**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-latest-1C3C3C?style=flat-square&logo=langchain&logoColor=white)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-00A6D6?style=flat-square)](https://faiss.ai)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## Overview

Enterprise RAG Intelligence is a production-style system designed for organizations that need secure, explainable, and grounded AI responses over private data. It combines semantic retrieval with strict role-based access control to ensure the right people see only the right information.

**Key capabilities:**
- Multi-source ingestion across PDFs, CSVs, and JSON logs
- Semantic retrieval using FAISS vector search
- Role-based document access enforcement before any response is generated
- Full source attribution and confidence scoring on every answer

---

## Architecture

```
User Query
    │
    ▼
┌─────────────────────┐
│  Semantic Retrieval  │  ← sentence-transformers + FAISS
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   RBAC Filtering    │  ← Department-level access control
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Context Aggregation │  ← Cross-source merging
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Response Generation│  ← Grounded LLM output
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Citation + Score   │  ← Source attribution & confidence
└─────────────────────┘
```

---

## Features

### 🔍 Intelligent Retrieval
- Semantic search using `sentence-transformers`
- Cross-source retrieval across PDFs, CSVs, and JSON logs
- Query-aware context selection with FAISS vector indexing

### 🔒 Secure Access Control
- RBAC enforcement at retrieval time — before response generation
- Department-level access restrictions
- Sensitive document filtering based on user role

### 📊 Explainability
- Confidence scoring on every response
- Source attribution with document-level traceability
- Full retrieval audit trail

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| RAG Framework | LangChain |
| Vector Search | FAISS |
| Embeddings | HuggingFace sentence-transformers |
| Data Processing | Pandas |

---

## Dataset

The system is demonstrated on a synthetic enterprise dataset:

| Source | Format | Contents |
|---|---|---|
| Company Policies | `.pdf` | HR policies, compliance documents |
| Employee Records | `.csv` | Roles, departments, compensation |
| Audit Logs | `.json` | Security events, access history |

---

## Access Control

RBAC is enforced **before** any document is passed to the language model.

| Role | Access |
|---|---|
| **Admin** | All documents across all departments |
| **HR** | HR policies, employee records — no Finance or Security data |
| **Finance** | Salary records, financial reports — no HR or Security data |
| **Engineering** | Engineering logs and records only |

**Example enforcement:**
```
HR user queries "Show salary records"
  → Retrieved documents filtered by role
  → Finance salary docs excluded from context
  → Response grounded only on permitted sources
```

---

## Example Queries

```
Who handles payroll?
Show employee salary records
Show security incidents
Show engineering records
```

---

## Project Structure

```
enterprise-rag/
├── data/
│   ├── policies/          # PDF documents
│   ├── employees/         # CSV records
│   └── logs/              # JSON audit logs
├── src/
│   ├── ingestion.py       # Multi-source data loading
│   ├── embeddings.py      # Vector index creation
│   ├── retrieval.py       # FAISS semantic search
│   ├── rbac.py            # Role-based access filtering
│   ├── generator.py       # Grounded response generation
│   └── attribution.py     # Source citation + confidence
├── config/
│   └── roles.yaml         # RBAC role definitions
└── main.py
```

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-org/enterprise-rag.git
cd enterprise-rag

# Install dependencies
pip install -r requirements.txt

# Run the system
python main.py --query "Who handles payroll?" --role hr
```

---

## Security

All document retrieval is gated by RBAC before reaching the language model. This ensures:

- No unauthorized data is included in the LLM context
- Sensitive records are filtered at the retrieval layer, not the output layer
- Every response includes citations so answers can be verified against source documents

---

<div align="center">

Built for enterprise environments where accuracy, security, and explainability are non-negotiable.

</div>
