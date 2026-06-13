from flask import Flask, render_template, request
from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.resume_matcher import calculate_match_score
from utils.skill_gap import find_missing_skills
from utils.recommendations import generate_recommendations
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Get Job Description
    job_description = request.form["job_description"]

    # Get Uploaded Resume
    file = request.files["resume"]

    # Save Resume
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract Resume Text
    resume_text = extract_text_from_pdf(filepath)

    # Extract Skills
    skills = extract_skills(resume_text)

    # Match Score
    match_score = calculate_match_score(
        skills,
        job_description
    )

    # Missing Skills
    missing_skills = find_missing_skills(
        skills,
        job_description
    )

    # Recommendations
    recommendations = generate_recommendations(
        missing_skills
    )

    # Matched Skills Count
    matched_skills_count = 0

    for skill in skills:
        if skill not in missing_skills:
            matched_skills_count += 1

    # Missing Skills Count
    missing_skills_count = len(missing_skills)

    # ATS Verdict
    if match_score >= 75:
        verdict = "Excellent Match"

    elif match_score >= 50:
        verdict = "Good Match"

    else:
        verdict = "Needs Improvement"

    # Render Dashboard
    return render_template(
        "results.html",
        resume_text=resume_text,
        skills=skills,
        match_score=match_score,
        missing_skills=missing_skills,
        recommendations=recommendations,
        verdict=verdict,
        matched_skills_count=matched_skills_count,
        missing_skills_count=missing_skills_count
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )