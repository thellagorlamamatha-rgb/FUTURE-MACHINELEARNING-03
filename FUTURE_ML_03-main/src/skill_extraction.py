# Skills list
skills_list = [

    "python",
    "machine learning",
    "react",
    "javascript",
    "html",
    "css",
    "nodejs",
    "git",
    "mongodb",
    "sql",
    "tensorflow",
    "java",
    "c++",
    "django",
    "flask"
]

def extract_skills(text):

    found_skills = []

    # Find matching skills
    for skill in skills_list:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills