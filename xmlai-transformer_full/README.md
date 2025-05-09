# XML AI Transformer

AI-powered system to convert Japanese Word (docx) documents into JATS-compliant XML with high precision, supporting ruby annotations, footnotes, figures, and math expressions.

## 🔧 Features

- 📝 Convert selected parts of docx to XML
- 🧠 Uses python-docx for docx parsing
- 🖼 Returns JATS XML via FastAPI
- 🛠 Microservice architecture planned
- 🗄 Persistent storage via PostgreSQL and MongoDB

## 🚀 Quickstart

```bash
pip install -r requirements.txt
python main.py
```

## 🛠 Endpoints

- `POST /convert` : Upload a `.docx` file, receive JATS XML

## 📚 License

MIT
