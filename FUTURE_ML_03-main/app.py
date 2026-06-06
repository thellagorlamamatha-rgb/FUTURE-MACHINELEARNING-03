import pandas as pd

from src.preprocessing import clean_text
from src.skill_extraction import extract_skills
from src.ranking import calculate_similarity

# =====================================
# READ JOB DESCRIPTION
# =====================================

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()

job_description_clean = clean_text(
    job_description
)

job_skills = set(
    extract_skills(job_description_clean)
)

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv(
    "data/resumes/Resume/Resume.csv"
)

candidate_results = []

# =====================================
# FILTER TECH CATEGORIES
# =====================================

tech_categories = [

    "INFORMATION-TECHNOLOGY",
    "DESIGNER",
    "DIGITAL-MEDIA",
    "WEB DESIGNING",
    "JAVA DEVELOPER",
    "PYTHON DEVELOPER",
    "DEVOPS ENGINEER"
]

# =====================================
# PROCESS RESUMES
# =====================================

for index, row in df.iterrows():

    try:

        category = str(row['Category'])

        # Skip non-tech resumes
        if category.upper() not in tech_categories:
            continue

        resume_text = str(
            row['Resume_str']
        )

        cleaned_resume = clean_text(
            resume_text
        )

        resume_skills = set(
            extract_skills(cleaned_resume)
        )

        score = calculate_similarity(
            job_description_clean,
            cleaned_resume
        )

        missing_skills = (
            job_skills - resume_skills
        )

        matched_skills = (
            job_skills.intersection(
                resume_skills
            )
        )

        candidate_results.append({

            "category": category,

            "score": round(
                score * 100,
                2
            ),

            "matched_skills": list(
                matched_skills
            ),

            "missing_skills": list(
                missing_skills
            )
        })

    except:
        continue

# =====================================
# SORT RESULTS
# =====================================

candidate_results = sorted(

    candidate_results,

    key=lambda x: x['score'],

    reverse=True
)

# =====================================
# DISPLAY RESULTS
# =====================================

print("\n")
print("=" * 60)
print("AI RESUME SCREENING SYSTEM")
print("=" * 60)

for i, candidate in enumerate(
    candidate_results[:10],
    start=1
):

    print(f"\nRank #{i}")

    print(
        "Candidate Category:",
        candidate['category']
    )

    print(
        "Match Score:",
        candidate['score'],
        "%"
    )

    print(
        "Matched Skills:",
        ", ".join(
            candidate['matched_skills']
        )
    )

    if candidate['missing_skills']:

        print(
            "Missing Skills:",
            ", ".join(
                candidate['missing_skills']
            )
        )

    else:
        print(
            "Missing Skills: None"
        )

    print("-" * 60)