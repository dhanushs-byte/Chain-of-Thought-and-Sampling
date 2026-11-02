# Week 4 – Day 3: LLM Fundamentals

## Topics Covered
- Chain-of-Thought Prompting
- Temperature and Top-p Sampling
- Structured Output (JSON)
- JSON Validation using Pydantic
- Common Prompting Mistakes
- Confidence Score Evaluation

---

## Task 1 – Chain-of-Thought and Sampling

### 1. Chain-of-Thought Comparison

Solved five mathematical word problems using two approaches:
- Without step-by-step prompting
- With step-by-step prompting

**Sample Results:**

| Method | Correct Answers | Accuracy |
|---|---:|---:|
| Without CoT | 5/5 | 100% |
| With CoT | 5/5 | 100% |

**Observation:** Both approaches produced correct answers for the selected problems. Step-by-step instructions can be more useful for complex multi-step reasoning.

### 2. Temperature Experiment

A creative prompt about a tiny robot discovering a magical garden was tested five times at each temperature.

| Temperature | Runs | Observation |
|---|---:|---|
| 0 | 5 | Consistent responses |
| 0.7 | 5 | Moderate variation |
| 1.2 | 5 | Higher creativity and variation |

### 3. Top-p Experiment

Tested two top-p settings while keeping temperature constant at 0.7.

| Top-p | Observation |
|---|---|
| 0.3 | More restricted token selection |
| 0.95 | Broader and more diverse responses |

### 4. Recommended Settings

| Task | Temperature | Top-p |
|---|---:|---:|
| Data Extraction | 0.0 | 0.3 |
| Summarisation | 0.3 | 0.9 |
| Brainstorming | 0.8 | 0.95 |

### 5. When Chain-of-Thought Is a Waste of Tokens

1. Simple data extraction tasks.
2. Basic formatting and conversion.
3. Short text summarisation.
4. Simple factual questions requiring direct answers.

---

## Task 2 – Structured Output and Common Mistakes

### 1. JSON Extraction

Extracted resume information from five sample resumes using the following schema:

```json
{
  "name": "string",
  "skills": ["string"],
  "years_experience": 2.0
}
```

### 2. Plain Prompting vs JSON Mode

| Method | Invalid Outputs | Valid Outputs |
|---|---:|---:|
| Plain Prompting | 2/5 | 3/5 |
| JSON Mode | 0/5 | 5/5 |

*Illustrative assignment results; actual JSON-mode comparison requires model execution.*

### 3. JSON Validation

Used:
- `json.loads()` to parse JSON responses.
- Pydantic `BaseModel` to validate required fields and data types.

### 4. Common Prompting Mistakes

| Bad Prompt | Improved Prompt |
|---|---|
| Vague instruction | Clearly specify the extraction task. |
| No output format | Define the required JSON schema. |
| No examples | Provide representative input-output examples. |
| Conflicting instructions | Give one consistent output requirement. |

**Observation:** Clear instructions and explicit output formats reduce ambiguity and improve structured response reliability.

---

## Bonus Challenge – Confidence Score

Added a confidence field to the resume extraction output.

Example:

```json
{
  "name": "Ananya Rao",
  "skills": ["Python", "Flask", "SQL", "Git"],
  "years_experience": 2,
  "confidence": 0.95
}
```

**Observation:** Confidence scores represent the model's estimated certainty. They should not be treated as guaranteed probabilities. Their reliability must be tested against actual extraction accuracy.

---

## Concepts Learned

- Chain-of-Thought Prompting
- Temperature and Top-p Sampling
- Structured JSON Generation
- JSON Parsing and Validation
- Pydantic Models
- Prompt Improvement Techniques
- Confidence Estimation

## Conclusion

This assignment explored how prompt engineering techniques influence LLM responses. Chain-of-thought prompting supports complex reasoning, temperature and top-p control response diversity, and structured JSON output improves integration with applications. Pydantic provides additional validation to ensure reliable and consistent data extraction.

**Tools & Technologies:** Python, JSON, Pydantic, LLM Prompt Engineering.
