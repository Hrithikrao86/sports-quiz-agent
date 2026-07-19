# 🏆 AI Sports Quiz Generator

An AI-powered Sports Quiz Generator built with **Streamlit**, **ChromaDB**, **Gemini 2.5 Flash**, and **DuckDuckGo Search**.

The application generates interactive multiple-choice quizzes by combining historical sports facts with the latest sports news.

---

## 🚀 Features

- 🏏 Choose from multiple sports
- 📊 Select quiz difficulty (Easy, Medium, Hard)
- 🤖 AI-generated multiple-choice questions
- 📚 Historical facts using ChromaDB (RAG)
- 📰 Latest sports news using DuckDuckGo Search
- ✅ Instant answer checking
- 📈 Final score and percentage
- 🎉 Performance feedback

---

## 🛠️ Tech Stack

- Streamlit
- ChromaDB
- Google Gemini 2.5 Flash
- DuckDuckGo Search (DDGS)
- Python

---

## 📂 Project Structure

```
sports-quiz-agent/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── sports_facts.json
│
├── src/
│   ├── database.py
│   ├── llm.py
│   └── search.py
│
└── chroma_db/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Quiz Generation
- Quiz Results

---

## 👨‍💻 Author

Developed by **Hrithik Rao**