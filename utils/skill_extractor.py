def extract_skills(resume_text):

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

        "data analysis",
        "power bi",
        "tableau",

        "large language models",
        "llm",
        "agentic ai",
        "agent based workflows",
        "groq",
        "langchain"
    ]

    found_skills = []

    resume_text = resume_text.lower()

    for skill in skill_database:

        if skill in resume_text:
            found_skills.append(skill)

    return found_skills