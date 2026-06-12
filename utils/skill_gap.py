def find_missing_skills(
    resume_skills,
    job_description
):

    jd_text = job_description.lower()

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

    jd_skills = []

    for skill in skill_database:

        if skill in jd_text:
            jd_skills.append(skill)

    missing_skills = []

    for skill in jd_skills:

        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills