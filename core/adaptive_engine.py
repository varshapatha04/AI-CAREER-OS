
from core.ollama_client import ask_ollama


def generate_adaptive_plan(skill, score, weak_topics):

    topics = ", ".join(weak_topics)

    prompt = f"""
You are an adaptive AI career mentor.

The student is learning:

SKILL:
{skill}

QUIZ SCORE:
{score}

WEAK TOPICS:
{topics}

Analyze the student's performance.

Create a personalized recovery plan.

If the score is below 60 percent:
- Focus strongly on the weak topics.
- Recommend revision before moving forward.
- Give simple practice tasks.

If the score is between 60 and 80 percent:
- Recommend targeted revision.
- Give moderate practice.
- Allow the student to continue gradually.

If the score is above 80 percent:
- Consider the skill mostly understood.
- Recommend moving to the next level.
- Suggest a practical project task.

Return:

PERFORMANCE:
Strong / Moderate / Needs Improvement

WEAK AREAS:
- topic

WHAT TO REVISE:
- topic

PRACTICE TASKS:
1. task
2. task
3. task

NEXT STEP:
Explain what the student should learn or practice next.

IMPORTANT:
Keep the recommendations practical for a college student.
"""

    result = ask_ollama(prompt)

    return result

