# 🧠 Business Assistant Bot

A simple, interactive Streamlit chatbot that answers business-related questions and creates GitHub support tickets when it can't find an answer.

---

## 🚀 Features

- ❓ **Ask Questions** — Type your question and get instant info (working hours, location, contact, etc.)
- 🤖 **Keyword Matching** — Bot uses keywords to return predefined answers.
- 🐞 **Raise a Ticket** — If no answer is found, you can submit a support ticket directly to GitHub Issues via API.

---

## 🛠 Built With

- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)
- [GitHub API](https://docs.github.com/en/rest/issues/issues)

---

## 💻 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/business-assistant-bot.git
cd business-assistant-bot

# 2. Create virtual environment and activate
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
