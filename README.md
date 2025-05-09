# 📧 AI-Powered Email Summarizer (n8n + Gemini)

This project automates the process of summarizing incoming Gmail emails using Google Gemini AI. The workflow is built in n8n and uses a Python script to generate summaries. The final output can be posted to Slack, emailed, or stored locally.

---

## 🚀 How It Works

1️⃣ **Trigger:** Listens for new emails in your Gmail inbox (can be filtered by label if desired).
2️⃣ **Processing:**
   - Extracts the subject, sender, and email body using a Code Node in n8n.
   - Passes the email body to a Python script via an Execute Command Node.
   - The Python script summarizes the email using Google Gemini.
3️⃣ **Output:**
   - The summary is combined with the original email info.
   - Can be posted to Slack, emailed, or viewed in n8n logs.

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/email-summarizer-n8n.git
cd email-summarizer-n8n
