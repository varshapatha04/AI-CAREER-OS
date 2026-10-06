
import streamlit as st
import json

from core.quiz_engine import generate_quiz
from core.adaptive_engine import generate_adaptive_plan


st.set_page_config(
    page_title="Quiz Arena",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Quiz Arena")
st.subheader(
    "Test your knowledge and discover your weak areas."
)


# -------------------------------
# Choose Skill
# -------------------------------

skill = st.selectbox(
    "🎯 Choose a skill",
    [
        "Python",
        "SQL",
        "Excel",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Statistics",
        "Data Structures and Algorithms",
        "Git and GitHub"
    ]
)


# -------------------------------
# Choose Difficulty
# -------------------------------

difficulty = st.selectbox(
    "📈 Choose difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


# -------------------------------
# Generate Quiz
# -------------------------------

if st.button("🚀 Generate Quiz"):

    with st.spinner("🧠 AI is creating your quiz..."):

        try:
            quiz_text = generate_quiz(skill, difficulty)

            # Handle possible Markdown code fences
            cleaned_text = quiz_text.strip()

            if cleaned_text.startswith("```"):
                cleaned_text = cleaned_text.split("\n", 1)[1]
                cleaned_text = cleaned_text.rsplit("```", 1)[0].strip()

            quiz = json.loads(cleaned_text)

            if len(quiz.get("questions", [])) != 5:
                st.error("AI did not generate exactly 5 questions.")
            elif not all(
                len(q.get("options", [])) == 4
                and isinstance(q.get("answer"), int)
                and 0 <= q["answer"] < 4
                and "topic" in q
                for q in quiz["questions"]
            ):
                st.error("The quiz format is invalid. Please generate it again.")
            else:
                st.session_state.quiz = quiz
                st.session_state.answers = {}
                st.session_state.quiz_skill = skill
                st.session_state.quiz_difficulty = difficulty
                st.session_state.quiz_submitted = False
                st.session_state.weak_topics = []
                st.session_state.quiz_score = None

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            st.error(
                "AI returned an invalid quiz format. "
                "Please click Generate Quiz again."
            )

        except Exception as error:
            st.error(f"Could not generate quiz: {error}")


# -------------------------------
# Display Quiz
# -------------------------------

if "quiz" in st.session_state:

    questions = st.session_state.quiz["questions"]
    quiz_skill = st.session_state.quiz_skill

    st.divider()
    st.header(f"🎯 {quiz_skill} Quiz")

    with st.form("quiz_form"):

        for i, question in enumerate(questions):

            st.subheader(f"Question {i + 1}")
            st.write(question["question"])

            selected = st.radio(
                "Choose your answer:",
                question["options"],
                index=None,
                key=f"question_{i}"
            )

            st.session_state.answers[i] = selected

        submitted = st.form_submit_button("✅ Submit Quiz")

    # -------------------------------
    # Evaluate Answers
    # -------------------------------

    if submitted:

        score = 0
        weak_topics = []

        for i, question in enumerate(questions):

            selected_answer = st.session_state.answers.get(i)
            correct_index = question["answer"]
            correct_answer = question["options"][correct_index]

            if selected_answer == correct_answer:
                score += 1
            else:
                topic = question.get("topic", "General concepts")
                weak_topics.append(topic)

        # Remove duplicate weak topics
        weak_topics = list(dict.fromkeys(weak_topics))

        total_questions = len(questions)
        percentage = (score / total_questions) * 100

        # Save results for other pages
        st.session_state.quiz_score = score
        st.session_state.quiz_percentage = percentage
        st.session_state.weak_topics = weak_topics
        st.session_state.quiz_submitted = True

    # -------------------------------
    # Show Results
    # -------------------------------

    if st.session_state.get("quiz_submitted", False):

        score = st.session_state.quiz_score
        percentage = st.session_state.quiz_percentage
        weak_topics = st.session_state.weak_topics

        st.divider()
        st.header("📊 Your Result")

        st.success(
            f"You scored {score}/{len(questions)} "
            f"({percentage:.0f}%)"
        )

        if percentage >= 80:
            st.success(
                "🔥 Excellent! You have a strong understanding of this skill."
            )
        elif percentage >= 60:
            st.warning(
                "👍 Good progress! You need some targeted revision."
            )
        else:
            st.error(
                "📚 You need more practice before moving forward."
            )

        # -------------------------------
        # Weak Areas
        # -------------------------------

        if weak_topics:

            st.subheader("🔍 Your Weak Areas")

            for topic in weak_topics:
                st.warning(f"📌 {topic}")

            # -------------------------------
            # Adaptive Learning Plan
            # -------------------------------

            if st.button("🔄 Generate Adaptive Learning Plan"):

                with st.spinner(
                    "🤖 AI is creating your personalized recovery plan..."
                ):

                    try:
                        adaptive_plan = generate_adaptive_plan(
                            quiz_skill,
                            percentage,
                            weak_topics
                        )

                        st.session_state.adaptive_plan = adaptive_plan

                    except Exception as error:
                        st.error(
                            f"Could not generate learning plan: {error}"
                        )

            if "adaptive_plan" in st.session_state:
                st.divider()
                st.header("🔄 Your Adaptive Learning Plan")
                st.write(st.session_state.adaptive_plan)

            st.info(
                "💡 Your weak topics are saved. "
                "Open AI Project Lab to generate projects for these areas."
            )

        else:

            st.success(
                "🎉 Amazing! No weak areas detected in this quiz."
            )

            st.info(
                "🚀 You are ready to move to the next level."
            )  