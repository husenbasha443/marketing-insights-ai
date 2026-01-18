# 📊 Marketing Insights AI

## 📌 Project Overview

**Marketing Insights AI** is an AI-powered customer feedback analysis system designed to convert raw, unstructured customer feedback into **actionable marketing insights**.

The system intelligently compares a **rule-based baseline approach** with an **Azure OpenAI–powered intelligent approach**, clearly demonstrating how Large Language Models (LLMs) enhance real-world business analysis.

This project is built as a **learning + academic submission project** and is suitable for **demos, viva explanations, interviews, and Azure-based evaluations**.

---

## 🎯 Objectives

* Analyze customer feedback text
* Detect customer sentiment (positive, negative, neutral)
* Extract key themes from feedback
* Identify customer complaints
* Suggest improvements
* Compare **baseline rules vs Azure OpenAI intelligence**
* Produce consistent **structured JSON output**

---

## 🧠 Problem Statement

Marketing teams receive large volumes of customer feedback from reviews, surveys, and support tickets.

Manual analysis is:

* Time-consuming
* Subjective
* Error-prone

This system solves the problem by transforming **unstructured feedback text** into **structured, machine-readable insights** using a hybrid AI approach.

---

## 🏗️ System Architecture

```
Customer Feedback (Text)
        ↓
Baseline Rule Engine (Keyword Logic)
        ↓
Confidence Check
        ↓
If Confidence HIGH → Return Baseline Result
        ↓
If Confidence LOW
        ↓
Azure OpenAI (LLM Analysis)
        ↓
Final Structured Output (JSON)
```

---

## 📂 Project Structure

```
marketing-insights-ai/
│
├── README.md
├── app.py                  # Streamlit UI
├── main.py                 # CLI execution
├── baseline.py             # Rule-based logic
├── openai_client.py        # Azure OpenAI integration
├── requirements.txt
├── .env                    # Environment variables
└── .venv/                  # Virtual environment
```

---

## 🧾 Required Output Format

Each customer feedback message is converted into the following strict JSON format:

```json
{
  "sentiment": "positive | negative | neutral",
  "themes": [],
  "complaints": [],
  "suggestions": []
}
```

---

## 🏷️ Sentiment Types

| Sentiment | Meaning                 |
| --------- | ----------------------- |
| Positive  | Satisfaction, praise    |
| Negative  | Dissatisfaction, issues |
| Neutral   | Informational or mixed  |

---

## 🧠 Baseline Rule-Based Logic

The baseline system uses simple keyword-based rules such as:

* `good`, `excellent` → Positive sentiment
* `bad`, `worst` → Negative sentiment
* `late`, `delay` → Delivery complaint
* `quality` → Product quality theme

### Purpose of Baseline

* Acts as a **non-AI benchmark**
* Fast and cost-efficient
* Highlights limitations of rule-based systems
* Demonstrates why AI fallback is needed

---

## 🤖 Azure OpenAI (AI-Based Logic)

Azure OpenAI (via **Azure AI Foundry**) is used when baseline confidence is **LOW**.

The LLM:

* Understands context and mixed sentiment
* Extracts themes beyond keywords
* Identifies implicit complaints
* Suggests meaningful improvements

### Advantages

* High accuracy
* Context awareness
* Handles edge cases
* Enterprise scalability

---

## 🧠 Prompt Design (Azure AI Foundry – Chat Playground)

### System Prompt

```
You are a marketing insights analyzer.

Your task is to analyze customer feedback and return structured insights.

You must:
- Determine sentiment
- Extract key themes
- Identify complaints
- Suggest improvements

Return ONLY valid JSON in the following format:

{
  "sentiment": "",
  "themes": [],
  "complaints": [],
  "suggestions": []
}

Do not include explanations or extra text.
```

---

## 🧪 Sample Test Inputs

```
The delivery was late but the product quality is excellent.
```

```
The software features are powerful, but onboarding documentation is confusing.
```

```
Great experience overall, but customer support response time could improve.
```

---

## 📊 Baseline vs Azure OpenAI Comparison

| Feature               | Baseline  | Azure OpenAI |
| --------------------- | --------- | ------------ |
| Speed                 | Very Fast | Moderate     |
| Accuracy              | Medium    | High         |
| Context Understanding | Low       | High         |
| Edge Case Handling    | Poor      | Excellent    |
| Cost                  | Free      | Token-based  |

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/husenbasha443/marketing-insights-ai.git
cd marketing-insights-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables (`.env`)

```env
AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.cognitiveservices.azure.com
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_MODEL=gpt-4o-mini
AZURE_OPENAI_API_VERSION=2024-07-18
```

---

## ▶️ Run Application

### CLI Mode

```bash
python main.py
```

### Streamlit UI

```bash
streamlit run app.py
```

---

## 🎓 What This Project Demonstrates

* Azure OpenAI usage via Azure AI Foundry
* Hybrid AI system design
* Prompt engineering best practices
* Baseline vs LLM comparison
* Enterprise-ready architecture

---

## 👤 Author

**Husen Basha**


