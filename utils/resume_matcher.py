def calculate_match_score(
    resume_skills,
    job_description
):

    skill_database = [

        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "html",
        "css",

        "sql",
        "mysql",
        "mongodb",

        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",

        "tensorflow",
        "keras",
        "pytorch",
        "scikit-learn",

        "flask",
        "django",
        "react",

        "git",
        "github",

        "aws",
        "azure",

        "docker",
        "kubernetes",

        "power bi",
        "tableau"
    ]

    jd_text = job_description.lower()

    jd_skills = []

    for skill in skill_database:

        if skill in jd_text:
            jd_skills.append(skill)

    if len(jd_skills) == 0:
        return 0

    matched_skills = 0

    for skill in jd_skills:

        if skill in resume_skills:
            matched_skills += 1

    score = round(
        (matched_skills / len(jd_skills)) * 100,
        2
    )

    return score