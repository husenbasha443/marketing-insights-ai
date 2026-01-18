# Customer Feedback Triage System

## 📌 Project Overview

The **Customer Feedback Triage System** is an AI-powered text-to-decision application designed to automatically classify, prioritize, and route customer feedback. The system compares a **rule-based baseline approach** with an **Azure OpenAI–powered intelligent approach** to demonstrate the value of Large Language Models (LLMs) in real-world enterprise decision-making.

This project is built as part of a **weekend assignment / learning project** and is suitable for demos, interviews, and academic submissions.

---

## 🎯 Objectives

* Automatically classify customer feedback into predefined categories
* Assign urgency levels based on business impact
* Suggest the next best action for support teams
* Compare traditional rule-based logic with Azure OpenAI results
* Ensure consistent, explainable, and scalable decision-making

---

## 🧠 Problem Statement

Organizations receive hundreds of customer messages daily. Not all messages require the same urgency or action. Manual triage is slow and inconsistent.

This system solves the problem by converting **unstructured text feedback** into **structured triage decisions**.

---

## 🏗️ System Architecture

```
Customer Feedback (Text)
        ↓
Preprocessing
        ↓
Baseline Rule Engine (if-else)
        ↓
Azure OpenAI (LLM Classification)
        ↓
Result Comparison
        ↓
Final Structured Output (JSON)
```

---

## 📂 Project Structure

```
customer-feedback-triage/
│
├── README.md
├── baseline/
│   └── rule_engine.py          # Rule-based classification logic
│
├── ai/
│   ├── prompt.txt              # Azure OpenAI system prompt
│   └── openai_client.py        # Azure OpenAI integration
│
├── app/
│   └── app.py                  # Main application (CLI / Streamlit)
│
├── data/
│   └── sample_feedback.json    # Test customer messages
│
├── requirements.txt
└── .env                        # Environment variables
```

---

## 🧾 Required Output Format

Every customer feedback message is converted into the following strict JSON format:

```json
{
  "category": "Complaint | Feature Request | Praise | Question",
  "urgency_level": "Low | Medium | High",
  "suggested_action": "Respond | Escalate | Ignore | Forward",
  "reasoning": "Explanation for the decision"
}
```

---

## 🏷️ Classification Categories

| Category        | Description                           |
| --------------- | ------------------------------------- |
| Complaint       | Issues, bugs, errors, dissatisfaction |
| Feature Request | Suggestions for new features          |
| Praise          | Positive feedback and appreciation    |
| Question        | Requests for information or help      |

---

## ⏱️ Urgency Levels

| Level  | Meaning                          |
| ------ | -------------------------------- |
| Low    | Can wait, minimal impact         |
| Medium | Needs timely attention           |
| High   | Critical business or user impact |

---

## 🚦 Suggested Actions

| Action   | Description                  |
| -------- | ---------------------------- |
| Respond  | Normal support response      |
| Escalate | Send to higher-level support |
| Ignore   | No action required           |
| Forward  | Route to another team        |

---

## 🧱 Baseline Rule-Based Logic

The baseline system uses keyword-based rules such as:

* Keywords like `crash`, `error`, `failed` → Complaint + High urgency
* Keywords like `add`, `feature`, `request` → Feature Request
* Keywords like `thank you`, `great`, `awesome` → Praise
* Sentences ending with `?` → Question

### Purpose of Baseline

* Acts as a non-AI benchmark
* Enables comparison with Azure OpenAI
* Highlights limitations of rule-based systems

---

## 🤖 Azure OpenAI (AI-Based Logic)

Azure OpenAI uses a Large Language Model to:

* Understand context and sentiment
* Handle mixed or ambiguous messages
* Provide reasoning for decisions

### Advantages

* Better accuracy
* Context awareness
* Explainable decisions
* Scales easily

---

## 🧠 Prompt Design (Azure AI Foundry – Chat Playground)

### System Prompt

```
You are an intelligent Customer Feedback Triage System used by an enterprise support team.

Your task is to analyze a single customer feedback message and convert it into a structured triage decision.

You must classify the feedback into exactly one category, determine its urgency level, suggest the most appropriate action, and clearly explain your reasoning.

You must strictly follow the allowed values and output format.

----------------------------------
ALLOWED CATEGORIES:
- Complaint
- Feature Request
- Praise
- Question

ALLOWED URGENCY LEVELS:
- Low
- Medium
- High

ALLOWED ACTIONS:
- Respond
- Escalate
- Ignore
- Forward
----------------------------------

DECISION RULES:
- Complaints related to payments, security, data loss, or service outages should usually be High urgency.
- Feature requests are typically Medium or Low urgency unless they block core functionality.
- Praise messages are Low urgency and usually require no action.
- Questions should be Responded to unless they indicate a serious issue.

You must infer intent even if the message contains mixed sentiment or unclear wording.

----------------------------------
OUTPUT FORMAT (STRICT JSON ONLY):

{
  "category": "<Complaint | Feature Request | Praise | Question>",
  "urgency_level": "<Low | Medium | High>",
  "suggested_action": "<Respond | Escalate | Ignore | Forward>",
  "reasoning": "<short clear explanation>"
}

Do not include any text outside the JSON object.
```

---

## 🧪 Sample Test Inputs

```
The app keeps crashing when I try to make a payment.
```

```
Can you please add a dark mode feature?
```

```
Great service! Very happy with the support team.
```

```
How can I reset my password?
```

---

## 📊 Comparison: Baseline vs Azure OpenAI

| Feature               | Baseline | Azure OpenAI |
| --------------------- | -------- | ------------ |
| Accuracy              | Medium   | High         |
| Context Understanding | Low      | High         |
| Edge Case Handling    | Poor     | Excellent    |
| Explainability        | Limited  | Strong       |
| Scalability           | Limited  | High         |

---

## 📈 Metrics (Optional Enhancements)

* Classification accuracy
* AI vs baseline disagreement rate
* Response time
* Edge case success rate

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/husenbasha443/Customer-Feedback-Triage-System.git
cd customer-feedback-triage
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables (.env)

```
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_KEY=your_key
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
```

---


## 👤 Author

**Husen Basha**


