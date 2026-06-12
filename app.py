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

    job_description = request.form["job_description"]

    file = request.files["resume"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    resume_text = extract_text_from_pdf(filepath)

    skills = extract_skills(resume_text)

    match_score = calculate_match_score(
    skills,
    job_description
)

    missing_skills = find_missing_skills(
        skills,
        job_description
    )

    recommendations = generate_recommendations(
        missing_skills
    )

    if match_score >= 75:
        verdict = "Excellent Match"

    elif match_score >= 50:
        verdict = "Good Match"

    else:
        verdict = "Needs Improvement"

    return render_template(
        "results.html",
        resume_text=resume_text,
        skills=skills,
        match_score=match_score,
        missing_skills=missing_skills,
        recommendations=recommendations,
        verdict=verdict
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )