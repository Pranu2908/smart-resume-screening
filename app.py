from flask import Flask, render_template, request
from utils.pdf_extractor import extract_text_from_pdf
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Get uploaded file
    file = request.files["resume"]

    # Save file
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # Extract text from PDF
    resume_text = extract_text_from_pdf(filepath)

    # Send extracted text to results page
    return render_template(
        "results.html",
        resume_text=resume_text
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True
    )