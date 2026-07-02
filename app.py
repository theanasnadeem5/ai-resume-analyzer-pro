from flask import Flask, render_template, request
import os
from utils.parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.jd_matcher import match_job_description
from utils.ats_engine import calculate_ats_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]
    job_description = request.form.get("job_description")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    resume_text = extract_text_from_pdf(filepath)
    skills = extract_skills(resume_text)
    match_percentage = match_job_description(resume_text, job_description)
    ats_score = calculate_ats_score(skills, match_percentage)

    return render_template(
        "result.html",
        skills=skills,
        ats_score=ats_score,
        match_percentage=match_percentage
    )

if __name__ == "__main__":
    app.run(debug=True)
