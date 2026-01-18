import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# --------------------------------------------------
# Azure OpenAI Client
# --------------------------------------------------
client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# --------------------------------------------------
# Baseline Rule-Based Analyzer
# --------------------------------------------------
def run_baseline(text: str):
    text_lower = text.lower()

    sentiment = "neutral"
    complaints = []
    themes = []
    suggestions = []
    confidence = "LOW"

    if "good" in text_lower or "excellent" in text_lower:
        sentiment = "positive"
        confidence = "HIGH"

    if "bad" in text_lower or "worst" in text_lower:
        sentiment = "negative"
        confidence = "HIGH"

    if "late" in text_lower or "delay" in text_lower:
        complaints.append("delay issue")
        themes.append("timeliness")
        confidence = "HIGH"

    if "quality" in text_lower:
        themes.append("quality")

    return {
        "sentiment": sentiment,
        "themes": list(set(themes)),
        "complaints": complaints,
        "suggestions": suggestions,
        "confidence": confidence
    }

# --------------------------------------------------
# Azure OpenAI Analyzer
# --------------------------------------------------
def analyze_with_openai(feedback: str):
    response = client.chat.completions.create(
        model=AZURE_OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a customer feedback analyzer. "
                    "Return ONLY valid JSON with keys: "
                    "sentiment, themes, complaints, suggestions."
                )
            },
            {"role": "user", "content": feedback}
        ],
        temperature=0
    )

    return response.choices[0].message.content

# --------------------------------------------------
# Hybrid Analyzer (Baseline → AI fallback)
# --------------------------------------------------
def analyze_feedback(feedback: str):
    baseline_result = run_baseline(feedback)

    if baseline_result["confidence"] == "HIGH":
        baseline_result.pop("confidence")
        return baseline_result

    ai_result = analyze_with_openai(feedback)
    return json.loads(ai_result)

# --------------------------------------------------
# Run Example
# --------------------------------------------------
if __name__ == "__main__":
    feedback = (
        "The room was clean and spacious, "
        "but check-in took too long and staff seemed untrained."
    )

    result = analyze_feedback(feedback)
    print(json.dumps(result, indent=2))