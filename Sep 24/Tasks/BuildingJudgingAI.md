# 🧠 Task: “Build & Judge a Mini AI”

---

## 📅 Part 1 — Chronology of AI

Write one real-world example for each stage:

| Stage            | Real-World Example                  |
|------------------|-------------------------------------|
| Machine Learning | Loan approval prediction            |
| Deep Learning    | Stock price trend prediction        |
| Computer Vision  | Tumor segmentation                  |
| NLP              | Voice assistants                    |
| LLMs             | ChatGPT                             |

---

## 🧬 Part 2 — Deep Learning Architectures

### 🔗 Match the model to the use case:

| Model       | Use Case                              |
|-------------|----------------------------------------|
| RNN         | Early speech-to-text systems           |
| LSTM        | Text translation (old Google Translate)|
| CNN         | Image recognition                      |
| Transformer | Predicting the next word in ChatGPT    |

### 🎯 Use Cases:
- Image recognition  
- Text translation (old Google Translate)  
- Predicting the next word in ChatGPT  
- Early speech-to-text systems  

---

## 🧰 Part 3 — Frameworks
### Choose one framework (PyTorch / TensorFlow / Keras). In one sentence, explain why you would use it if you were a student making a cat-vs-dog classifier.

**Chosen Framework:** PyTorch  
**Why?** Because it is simple, pythonic design makes experimenting and debugging easy for beginners like students.

---

## 📊 Part 4 — Evaluation Metrics

Imagine you built a spam filter. Answer:

- **Precision:**  
  If it marks 10 emails as spam and 7 are truly spam
  → \( \frac{7}{10} = 0.7 \) → **70%**

- **Recall:**  
  If there were 12 spam emails in total, how many did it catch?  
  → \( \frac{7}{12} = 0.5833 \) → **58.33%**

- **F1 Score:**  
  Use the formula:  
  \( F1 = \frac{2 \times (Precision \times Recall)}{Precision + Recall} \)  
  → \( \frac{2 \times (0.70 \times 0.58)}{0.70 + 0.58} = \frac{2 \times 0.406}{1.28} = 0.63 \)  
  → **F1 Score = 0.63**

- **MSE / MAE:**  
  Predict your friend’s age (actual = 15, prediction = 18)  
  → Error = 3  
  → MAE = \( |3| = 3 \)  
  → MSE = \( 3^2 = 9 \)  
  → **MSE punishes the error more**

- **BLEU / ROUGE:**  
  AI translated “The cat sat on the mat” as “Cat is on the mat.”  
  → **ROUGE** would give a higher score due to better recall of key phrases.

---

## 🧭 Part 5 — Responsible AI & Explainability

You built an AI that predicts loan approvals.  
A customer asks, “Why was my loan rejected?”

### 🗣️ Fair Explanation:
1. Your loan was evaluated using factors like income, existing debts, and credit history.  
2. The model compared your profile with others who successfully repaid loans.  
3. One key factor was that your income was too low compared to the loan amount requested.  
4. This increased the risk that repayments could be difficult.  
5. That’s why the system suggested rejecting this application.  
6. This decision is based on data patterns, not personal bias.  
7. You may reapply if your financial situation improves.

---
