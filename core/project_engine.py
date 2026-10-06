from core.ollama_client import ask_ollama


def generate_projects(target_role, skill_gap, weak_topics):

    topics = ", ".join(weak_topics)

    prompt = f"""
You are an expert AI career mentor and project advisor.

The student wants to become:

TARGET ROLE:
{target_role}

Here is the student's skill gap:

SKILL GAP:
{skill_gap}

The student's weak quiz topics are:

WEAK TOPICS:
{topics}

Your task is to recommend practical projects that help the student
close their skill gaps and improve their weak areas.

Generate exactly 3 project ideas.

For each project provide:

PROJECT 1

PROJECT NAME:
Give a creative project name.

WHY THIS PROJECT:
Explain why this project is useful for the student's target role.

SKILLS USED:
List the important technical skills used.

SKILLS IMPROVED:
Explain which missing or weak skills this project improves.

PROJECT IDEA:
Explain what the student will build.

MAIN FEATURES:
1. Feature
2. Feature
3. Feature
4. Feature

DIFFICULTY:
Beginner / Intermediate / Advanced

ESTIMATED TIME:
Give a realistic number of days.

RESUME VALUE:
Explain why this project would look good on a resume.

TECH STACK:
List the technologies needed.


PROJECT 2

Use the same structure.


PROJECT 3

Use the same structure.


IMPORTANT:
- Projects must match the target role.
- Projects must address the student's actual skill gaps.
- Projects should improve the weak quiz topics.
- Avoid generic projects like a basic calculator or simple to-do app.
- Prefer real-world problems.
- Keep the projects realistic for a college student.
- Make the projects different from each other.
- Include AI only when it genuinely adds value.
"""

    result = ask_ollama(prompt)

    return result 
