import streamlit as st
import json
import os
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
# Streamlit UI
# --------------------------------------------------
st.set_page_config(
    page_title="Marketing Insights Analyzer",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Marketing Insights Analyzer")
st.caption("Baseline-first → Azure OpenAI fallback")

feedback = st.text_area(
    "📝 Enter customer feedback",
    height=120,
    placeholder="The service was excellent but delivery was late."
)

analyze = st.button("🔍 Analyze")

if analyze:
    if not feedback.strip():
        st.warning("Please enter customer feedback.")
    else:
        with st.spinner("Analyzing feedback..."):
            baseline_result = run_baseline(feedback)

            if baseline_result["confidence"] == "HIGH":
                st.success("✅ Processed using Baseline Logic")
                baseline_result.pop("confidence")
                result = baseline_result
            else:
                st.info("🤖 Baseline confidence low → Using Azure OpenAI")
                ai_result = analyze_with_openai(feedback)
                result = json.loads(ai_result)

        st.subheader("📌 Analysis Result")
        st.json(result)
