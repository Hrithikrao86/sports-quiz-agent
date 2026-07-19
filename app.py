import streamlit as st

from src.database import load_data, query_facts
from src.search import get_live_news
from src.llm import generate_quiz

st.set_page_config(
    page_title="🏆 AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Sports Quiz Generator")
st.caption("Generate AI-powered sports quizzes using historical facts and live sports news.")

load_data()

if "quiz" not in st.session_state:
    st.session_state.quiz = None

st.sidebar.header("⚙ Quiz Settings")

sport = st.sidebar.selectbox(
    "Choose Sport",
    ["Cricket", "Football", "Badminton"]
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.sidebar.button("🚀 Generate Quiz"):
    for key in list(st.session_state.keys()):
      if key.startswith("question_"):
        del st.session_state[key]
    with st.spinner("Generating AI Quiz..."):

        facts = query_facts(
            sport=sport,
            query_text=f"{sport} history",
            n_results=3
        )

        news = get_live_news(sport)
        news_text = "\n\n".join(item["body"] for item in news)

        st.session_state.quiz = generate_quiz(
            sport,
            difficulty,
            "\n".join(facts),
            news_text
        )

if st.session_state.quiz:

    st.success("✅ Quiz Generated Successfully!")

    for i, q in enumerate(st.session_state.quiz):

        with st.container(border=True):

            st.subheader(f"Question {i+1}")

            st.write(q["question"])

            st.radio(
                "Choose your answer",
                q["options"],
                index=None,
                key=f"question_{i}"
            )

    if st.button("🎯 Submit Quiz", use_container_width=True):
        missing = []

        for i in range(len(st.session_state.quiz)):
            if st.session_state.get(f"question_{i}") is None:
              missing.append(i + 1)

        if missing:
            st.warning(f"Please answer all questions before submitting. Missing: {missing}")
            st.stop()

        score = 0

        st.divider()
        

        

        st.header("🏆 Quiz Results")

        for i, q in enumerate(st.session_state.quiz):

            user_answer = st.session_state.get(f"question_{i}")

            with st.container(border=True):

                st.subheader(f"Question {i+1}")

                if user_answer == q["answer"]:
                    score += 1
                    st.success("✅ Correct")
                else:
                    st.error("❌ Wrong")

                st.write(f"**Your Answer:** {user_answer}")
                st.success(f"Correct Answer: {q['answer']}")

        percentage = (score / len(st.session_state.quiz)) * 100

        st.divider()

        st.header(f"🏆 Final Score: {score}/{len(st.session_state.quiz)}")

        st.progress(score / len(st.session_state.quiz))

        st.write(f"### Percentage: {percentage:.0f}%")

        if percentage == 100:
            st.balloons()
            st.success("🌟 Perfect Score!")
        elif percentage >= 80:
            st.success("🔥 Excellent Performance!")
        elif percentage >= 60:
            st.info("👍 Good Job!")
        else:
            st.warning("📚 Keep Practicing!")

        if st.button("🔄 Generate New Quiz"):

            st.session_state.quiz = None

            for key in list(st.session_state.keys()):
                if key.startswith("question_"):
                    del st.session_state[key]

            st.rerun()

st.caption("Built with ❤️ using Streamlit, ChromaDB, DuckDuckGo Search and Gemini 2.5 Flash")