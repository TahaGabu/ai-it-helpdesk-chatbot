import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="IT Helpdesk Chatbot", layout="centered")

# Load model
model = joblib.load("model/chatbot_model.pkl")

# Responses
responses = {
    "password_reset": "To reset your password, go to settings > reset password and follow the steps.",
    "login_issue": "Please check your credentials or clear cache. If the issue persists, contact support.",
    "ticket_status": "Please provide your ticket ID. This is a demo system.",
    "software_help": "Download from official website and follow installation steps.",
    "technical_issue": "Try restarting system or checking internet. Contact support if needed.",
    "greeting": "Hello! How can I assist you today?",
    "thanks": "You're welcome! 😊",
    "goodbye": "Goodbye! Have a great day!"
}

# Title
st.title("💬 IT Helpdesk Chatbot")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

if user_input is not None:
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Predict intent with confidence threshold for unknown queries
        data = pd.Series([user_input])
        fallback_reply = "Sorry, I didn't understand that."

        try:
            probs = model.predict_proba(data)
            confidence = max(probs[0])
        except Exception:
            # If probability output is unavailable, assume full confidence.
            confidence = 1.0

        if confidence < 0.3:
            bot_reply = fallback_reply
        else:
            prediction = model.predict(data)[0]
            bot_reply = responses.get(prediction, fallback_reply)

        # Show bot message
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.markdown(bot_reply)