
from core.ollama_client import ask_ollama


def analyze_skill_gap(resume_text, target_role):

    prompt = f"""
You are an expert AI career mentor.

Analyze the student's resume based on their target career role.

TARGET ROLE:
{target_role}

RESUME:
{resume_text}

Perform these tasks:

1. Identify the student's current technical skills.
2. Identify the important skills required for the target role.
3. Compare the current skills with the required skills.
4. Identify the missing skills.
5. Give each missing skill a priority: HIGH, MEDIUM, or LOW.
6. Estimate realistic learning days for each missing skill.
7. Explain why each missing skill is important.
8. Give the best order in which the student should learn the missing skills.

Return the result exactly in this structure:

CURRENT SKILLS:
- skill
- skill
- skill

REQUIRED SKILLS:
- skill
- skill
- skill

MISSING SKILLS:
- skill | HIGH | X days | reason
- skill | MEDIUM | X days | reason
- skill | LOW | X days | reason

LEARNING ORDER:
1. skill
2. skill
3. skill

TOTAL ESTIMATED TIME:
X days

IMPORTANT:
- Compare the resume with the target role carefully.
- Do not mark a skill as missing if it is already present in the resume.
- Do not add unnecessary technologies.
- Focus on skills that are actually useful for the target role.
- Keep the recommendations realistic for a college student.
"""

    result = ask_ollama(prompt)

    return result
