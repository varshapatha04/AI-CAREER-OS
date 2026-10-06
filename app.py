import streamlit as st

from core.resume_parser import extract_text_from_pdf
from core.ollama_client import ask_ollama
from core.skill_gap import analyze_skill_gap
from core.roadmap_engine import generate_roadmap


st.set_page_config(
    page_title="AI Career OS",
    page_icon="🚀",
    layout="wide"
)


st.title("🚀 AI Career OS")
st.subheader("Your AI-powered career companion")


# --------------------------------
# Initialize Career Memory
# --------------------------------

if "career_memory" not in st.session_state:

    st.session_state.career_memory = {
        "target_role": None,
        "resume_text": None,
        "resume_analysis": None,
        "skill_gap": None,
        "roadmap": None
    }


# --------------------------------
# Target Role
# --------------------------------

target_role = st.selectbox(
    "🎯 What is your target career?",
    [
        "Data Analyst",
        "Data Scientist",
        "AI Engineer",
        "Machine Learning Engineer",
        "Software Engineer",
        "Full Stack Developer",
        "Business Analyst"
    ]
)


# --------------------------------
# Resume Upload
# --------------------------------

resume = st.file_uploader(
    "📄 Upload your resume",
    type=["pdf"]
)


if resume:

    st.success("Resume uploaded successfully! ✅")


    if st.button("🚀 Analyze My Career"):

        # --------------------------------
        # STEP 1: Extract Resume
        # --------------------------------

        with st.spinner("📄 Reading your resume..."):

            resume_text = extract_text_from_pdf(resume)


        if not resume_text:

            st.error(
                "Could not extract text from the resume."
            )

        else:

            # Save resume + target role
            st.session_state.career_memory["target_role"] = target_role
            st.session_state.career_memory["resume_text"] = resume_text


            # --------------------------------
            # STEP 2: Resume Analysis
            # --------------------------------

            with st.spinner(
                "🦙 AI is analyzing your resume..."
            ):

                resume_prompt = f"""
You are an AI career mentor.

Analyze this student's resume.

Extract:

1. Programming languages
2. Technical skills
3. Tools
4. Projects
5. Education
6. Experience
7. Certifications

Keep the answer concise and structured.

Resume:

{resume_text}
"""

                resume_analysis = ask_ollama(
                    resume_prompt
                )


            # Save resume analysis

            st.session_state.career_memory[
                "resume_analysis"
            ] = resume_analysis


            st.divider()

            st.header("📄 Your Resume Profile")

            st.write(resume_analysis)


            # --------------------------------
            # STEP 3: Skill Gap
            # --------------------------------

            with st.spinner(
                "🧠 Finding your skill gaps..."
            ):

                skill_gap = analyze_skill_gap(
                    resume_text,
                    target_role
                )


            # Save skill gap

            st.session_state.career_memory[
                "skill_gap"
            ] = skill_gap


            st.divider()

            st.header("🎯 Your Skill Gap")

            st.write(skill_gap)


            # --------------------------------
            # STEP 4: Career Roadmap
            # --------------------------------

            with st.spinner(
                "🗺️ Building your personalized roadmap..."
            ):

                roadmap = generate_roadmap(
                    resume_text,
                    target_role,
                    skill_gap
                )


            # Save roadmap

            st.session_state.career_memory[
                "roadmap"
            ] = roadmap


            st.divider()

            st.header(
                "🗺️ Your Personalized Career Roadmap"
            )

            st.write(roadmap)


            # --------------------------------
            # Career Memory Status
            # --------------------------------

            st.success(
                "🧠 Career Memory updated successfully!"
            )  

              