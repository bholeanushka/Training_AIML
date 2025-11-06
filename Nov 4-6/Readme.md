# 🧠 InnovateTech Solutions – AI Onboarding Assistant

Welcome to the official repository for the InnovateTech AI Onboarding Assistant — a smart, conversational agent designed to streamline employee onboarding by answering questions, summarizing policy documents, and delivering personalized guidance.

---

## 📌 Problem Statement

Employee onboarding is often a manual, repetitive, and time-consuming process. HR teams are burdened with answering similar questions, sharing documents, and ensuring consistent communication across departments. This leads to:

- Inconsistent onboarding experiences
- Delayed access to company policies
- Reduced productivity for new hires
- Increased workload for HR personnel

**Solution:** An intelligent AI assistant that automates onboarding tasks, provides instant answers to employee queries, and delivers personalized support using company documents and employee profiles.

---

## 🤖 Project Type

This project is a hybrid AI assistant that functions as:

| Type        | Description |
|-------------|-------------|
| 💬 Chatbot  | Engages users in natural conversation |
| 📄 Summarizer | Extracts and summarizes key information from policy documents |
| 🔍 Analyzer | Retrieves relevant content from embedded PDFs using semantic search |

---

## 🏗️ Architecture Overview

```mermaid
graph TD
    A[Streamlit UI] --> B[AssistantGUI.py]
    B --> C[Assistant.py]
    C --> D[LangChain Chain]
    D --> E[Groq LLaMA 3 Model]
    D --> F[FAISS Vector Store]
    F --> G[PDF Policy Documents]
    C --> H[Employee Profile]
