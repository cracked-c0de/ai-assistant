import streamlit as st
import requests
import os

st.set_page_config(page_title="Business Assistant Bot")
st.header("🤖 Business Assistant Bot")

# GitHub config
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = "your-username/business-assistant-support"  # Change this!

# Your predefined responses
info = {
    "hours": "We’re open from 9 AM to 7 PM on weekdays, and from 10 AM to 4 PM on Saturdays.",
    "address": "Our main office is at Amir Temur Street, Tashkent, Block B2, 3rd Floor.",
    "location": "Find us in the heart of Tashkent, just beside the Amir Temur metro station.",
    "contact": "Reach us anytime at +998 91 456 78 90 or message us on Telegram.",
    "phone": "+998 91 456 78 90",
    "email": "hello@techhub.uz",
}

# Keywords related to each category
intents = {
    "hours": ["open", "closing", "working hours", "time", "when"],
    "address": ["address", "where exactly", "street", "building"],
    "location": ["located", "location", "where are you", "map", "place"],
    "contact": ["contact", "reach", "support", "get in touch", "talk"],
    "phone": ["call", "phone", "number", "mobile", "contact number"],
    "email": ["email", "mail", "write", "send email"],
}

question = st.text_input("📝 Ask your question:")

def match_intent(user_input):
    user_input = user_input.lower()
    scores = {intent: 0 for intent in intents}

    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                scores[intent] += 1

    # Get the best match
    best_intent = max(scores, key=scores.get)
    if scores[best_intent] > 0:
        return best_intent
    return None

if question:
    intent = match_intent(question)
    if intent and intent in info:
        st.success(info[intent])
    else:
        st.warning("🤔 I couldn't find an answer. You can raise a support ticket below.")
        with st.form("ticket_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Describe your issue")
            submit = st.form_submit_button("Submit Ticket")

            if submit:
                if name and email and message:
                    issue_title = f"Support Request from {name}"
                    issue_body = f"""
**Name:** {name}  
**Email:** {email}  
**Original Question:** {question}

**Message:**
{message}
"""
                    headers = {
                        "Authorization": f"token {GITHUB_TOKEN}",
                        "Accept": "application/vnd.github.v3+json"
                    }

                    res = requests.post(
                        f"https://api.github.com/repos/{GITHUB_REPO}/issues",
                        headers=headers,
                        json={"title": issue_title, "body": issue_body}
                    )

                    if res.status_code == 201:
                        st.success("✅ Ticket submitted successfully.")
                    else:
                        st.error(f"❌ Failed to submit ticket (status {res.status_code})")
                else:
                    st.error("Please complete all fields.")
