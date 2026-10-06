import streamlit as st

from core.project_engine import generate_projects


st.set_page_config(
    page_title="AI Project Lab",
    page_icon="💡",
    layout="wide"
)

st.title("💡 AI Project Lab")
st.subheader(
    "Build projects based on your career goals and weak areas."
)


# --------------------------------
# Get Career Memory
# --------------------------------

career_memory = st.session_state.get(
    "career_memory",
    {}
)

target_role = career_memory.get(
    "target_role"
)

skill_gap = career_memory.get(
    "skill_gap"
)


# --------------------------------
# Show Career Information
# --------------------------------

if target_role:

    st.success(
        f"🎯 Target Role: {target_role}"
    )

else:

    st.warning(
        "Please analyze your career from the Home page first."
    )


# --------------------------------
# Show Skill Gap
# --------------------------------

if skill_gap:

    st.subheader("📌 Your Skill Gap")

    st.write(skill_gap)

else:

    st.info(
        "No skill gap found yet."
    )


# --------------------------------
# Weak Topics From Quiz
# --------------------------------

weak_topics = st.session_state.get(
    "weak_topics",
    []
)


if weak_topics:

    st.subheader("🧠 Weak Topics From Quiz")

    for topic in weak_topics:

        st.warning(
            f"📌 {topic}"
        )

else:

    st.info(
        "Complete a Quiz to detect your weak topics."
    )


# --------------------------------
# Generate Projects
# --------------------------------

if st.button("🚀 Generate My Projects"):

    if not target_role:

        st.warning(
            "Please analyze your career first."
        )

    elif not skill_gap:

        st.warning(
            "Skill gap is not available yet."
        )

    elif not weak_topics:

        st.warning(
            "Complete a Quiz first."
        )

    else:

        with st.spinner(
            "🤖 AI is designing your personalized projects..."
        ):

            try:

                projects = generate_projects(
                    target_role,
                    skill_gap,
                    weak_topics
                )

                st.session_state.projects = projects

            except Exception as error:

                st.error(
                    f"Could not generate projects: {error}"
                )


# --------------------------------
# Display Projects
# --------------------------------

if "projects" in st.session_state:

    st.divider()

    st.header("🚀 Your Personalized Projects")

    st.write(
        st.session_state.projects
    ) 
    