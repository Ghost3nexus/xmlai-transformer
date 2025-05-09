# XML AI Transformer

AI-powered system to convert Japanese Word (docx) documents into JATS-compliant XML with high precision, supporting ruby annotations, footnotes, figures, and math expressions.

## 🔧 Features

- 📝 Convert selected parts of docx to XML
- 🧠 Uses LLMs (GPT), OCR (EasyOCR), and MathML transformers
- 🖼 Realtime XML preview and in-place editing (WIP)
- 🛠 Microservice architecture using FastAPI
- 🗄 Persistent storage via PostgreSQL and MongoDB

## 📦 Architecture

```plaintext
Frontend (Next.js + TipTap) ── Socket.IO ──▶ FastAPI (Python)
   │                                                │
   ├── docx-parser  ← python-docx                  │
   ├── ocr-module   ← EasyOCR                      │
   ├── mathml-conv  ← im2markup                    │
   └── xml-writer   ← manubot                      ▼
                        PostgreSQL / MongoDB (Docker)
```

## 🚀 Quickstart (with Dev Container)

```bash
git clone https://github.com/YOUR_USERNAME/xmlai-transformer.git
cd xmlai-transformer
code .
```

VS Code will automatically open in the right dev container.

## 🛠 Tech Stack

- Backend: FastAPI
- Frontend: Next.js (planned)
- AI: OpenAI GPT, EasyOCR, im2markup
- DB: PostgreSQL, MongoDB

## 📚 License

MIT
