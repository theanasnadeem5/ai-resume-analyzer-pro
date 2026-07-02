TECH_SKILLS = [
    "python",
    "java",
    "javascript",
    "docker",
    "aws",
    "flask",
    "django",
    "sql",
    "git",
    "github",
    "linux",
    "machine learning",
    "api",
    "react"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in TECH_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills
