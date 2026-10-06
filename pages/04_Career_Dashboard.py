import streamlit as st


st.set_page_config(
    page_title="Career Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Career Dashboard")
st.subheader(
    "Your complete AI-powered career progress."
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

resume_analysis = career_memory.get(
    "resume_analysis"
)

skill_gap = career_memory.get(
    "skill_gap"
)

roadmap = career_memory.get(
    "roadmap"
)


# --------------------------------
# Target Role
# --------------------------------

st.header("🎯 Career Goal")

if target_role:

    st.success(
        f"Target Role: {target_role}"
    )

else:

    st.warning(
        "Your target role is not set yet."
    )


# --------------------------------
# Career Overview
# --------------------------------

st.divider()

st.header("📌 Career Overview")

col1, col2, col3 = st.columns(3)


with col1:

    if resume_analysis:

        st.metric(
            "Resume Status",
            "Analyzed ✅"
        )

    else:

        st.metric(
            "Resume Status",
            "Not Analyzed"
        )


with col2:

    if skill_gap:

        st.metric(
            "Skill Gap",
            "Detected 🎯"
        )

    else:

        st.metric(
            "Skill Gap",
            "Not Available"
        )


with col3:

    if roadmap:

        st.metric(
            "Roadmap",
            "Created 🗺️"
        )

    else:

        st.metric(
            "Roadmap",
            "Not Created"
        )


# --------------------------------
# Quiz Performance
# --------------------------------

st.divider()

st.header("🧠 Quiz Performance")


quiz_score = st.session_state.get(
    "quiz_score"
)

quiz_percentage = st.session_state.get(
    "quiz_percentage"
)

weak_topics = st.session_state.get(
    "weak_topics",
    []
)


if quiz_percentage is not None:

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Latest Score",
            f"{quiz_score}/5"
        )

    with col2:

        st.metric(
            "Accuracy",
            f"{quiz_percentage:.0f}%"
        )


    if quiz_percentage >= 80:

        st.success(
            "🔥 Excellent performance!"
        )

    elif quiz_percentage >= 60:

        st.warning(
            "👍 Good progress. Keep practicing."
        )

    else:

        st.error(
            "📚 More practice is needed."
        )

else:

    st.info(
        "Complete a quiz to see your performance."
    )


# --------------------------------
# Weak Areas
# --------------------------------

st.divider()

st.header("⚠️ Weak Areas")


if weak_topics:

    for topic in weak_topics:

        st.warning(
            f"📌 {topic}"
        )

else:

    st.success(
        "🎉 No weak areas detected yet."
    )


# --------------------------------
# Projects
# --------------------------------

st.divider()

st.header("💡 AI Projects")


projects = st.session_state.get(
    "projects"
)


if projects:

    st.success(
        "Personalized projects generated ✅"
    )

    st.write(projects)

else:

    st.info(
        "Complete the Quiz and open AI Project Lab "
        "to generate personalized projects."
    )


# --------------------------------
# Roadmap
# --------------------------------

st.divider()

st.header("🗺️ Career Roadmap")


if roadmap:

    st.write(
        roadmap
    )

else:

    st.info(
        "Analyze your resume to generate your roadmap."
    )


# --------------------------------
# Resume Profile
# --------------------------------

st.divider()

st.header("📄 Resume Profile")


if resume_analysis:

    st.write(
        resume_analysis
    )

else:

    st.info(
        "Upload and analyze your resume from the Home page."
    )


# --------------------------------
# Career OS Status
# --------------------------------

st.divider()

st.header("🚀 Career OS Status")

completed_steps = 0
total_steps = 5


if resume_analysis:
    completed_steps += 1

if skill_gap:
    completed_steps += 1

if roadmap:
    completed_steps += 1

if quiz_percentage is not None:
    completed_steps += 1

if projects:
    completed_steps += 1


progress = completed_steps / total_steps


st.progress(progress)

st.write(
    f"Career OS Progress: "
    f"**{completed_steps}/{total_steps} steps completed**"
)


if completed_steps == total_steps:

    st.success(
        "🎉 Your Career OS is fully active!"
    )

else:

    st.info(
        "Keep completing the remaining steps to activate your Career OS."
    ) 
    