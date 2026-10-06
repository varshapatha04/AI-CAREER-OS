from core.ollama_client import ask_ollama


def generate_roadmap(resume_text, target_role, skill_gap):

    prompt = f"""
You are an expert AI career mentor.

Create a personalized career roadmap for this student.

TARGET ROLE:
{target_role}

RESUME:
{resume_text}

SKILL GAP:
{skill_gap}

Create a practical roadmap based on the student's actual skill gaps.

For each important missing skill, provide:

- Skill name
- Why it is needed
- Topics to learn
- Estimated learning time
- Practice task
- Mini project

Arrange the skills in the correct learning order.

Divide the roadmap into these phases:

PHASE 1 - FOUNDATION

PHASE 2 - CORE SKILLS

PHASE 3 - PROJECTS

PHASE 4 - INTERVIEW PREPARATION

At the end provide:

FINAL ROADMAP:
1. Skill
2. Skill
3. Skill

IMPORTANT:
- Do not add unnecessary technologies.
- Prioritize the student's actual skill gaps.
- Keep the roadmap realistic for a college student.
- Make the roadmap practical and project-oriented.
"""

    result = ask_ollama(prompt)

    return result

