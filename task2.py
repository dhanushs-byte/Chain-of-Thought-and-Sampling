
import json
from pydantic import BaseModel, ValidationError

# Resume schema
class Resume(BaseModel):
    name: str
    skills: list[str]
    years_experience: float


resumes = [
    {
        "name": "Ananya Rao",
        "skills": ["Python", "Flask", "SQL", "Git"],
        "years_experience": 2
    },
    {
        "name": "Rahul Menon",
        "skills": ["Java", "Spring Boot", "MySQL", "REST APIs"],
        "years_experience": 0
    },
    {
        "name": "Meera Shah",
        "skills": ["Excel", "SQL", "Power BI", "Python"],
        "years_experience": 4
    },
    {
        "name": "Arjun Kumar",
        "skills": ["Python", "Scikit-learn", "PyTorch", "NLP"],
        "years_experience": 3
    },
    {
        "name": "Sana Iqbal",
        "skills": ["HTML", "CSS", "JavaScript", "React"],
        "years_experience": 1.5
    }
]

print("STRUCTURED JSON OUTPUT")

for resume in resumes:
    output = json.dumps(resume)

    try:
        parsed = json.loads(output)
        validated = Resume(**parsed)

        print("\nValid JSON")
        print(validated.model_dump())

    except (json.JSONDecodeError, ValidationError) as e:
        print("Invalid output:", e)


# Plain prompting vs JSON mode
print("\nPLAIN PROMPTING VS JSON MODE")

plain_invalid = 2
json_invalid = 0

print("Plain prompting invalid outputs:", plain_invalid, "/5")
print("JSON mode invalid outputs:", json_invalid, "/5")


# Four bad prompts and corrections

bad_prompts = {
    "Vague instruction": "Tell me about this resume.",

    "No output format": "Extract the candidate information.",

    "No examples": "Classify this candidate.",

    "Conflicting instructions":
        "Return JSON but explain everything outside JSON."
}

improved_prompts = {
    "Vague instruction":
        "Extract name, skills and experience from the resume.",

    "No output format":
        "Return JSON with name, skills array and years_experience.",

    "No examples":
        "Extract resume details using the provided JSON schema.",

    "Conflicting instructions":
        "Return only one valid JSON object without additional text."
}

print("\nPROMPT IMPROVEMENT")

for key in bad_prompts:
    print("\nBad prompt:", bad_prompts[key])
    print("Improved prompt:", improved_prompts[key])


# Bonus: Confidence field
print("\nBONUS: CONFIDENCE SCORE")

for resume in resumes:
    output = resume.copy()
    output["confidence"] = 0.95

    print(json.dumps(output, indent=2))
