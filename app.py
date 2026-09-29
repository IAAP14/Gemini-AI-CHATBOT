import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="💗",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f6, #ffe4ef);
    font-family: Arial, sans-serif;
}

.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

h1 {
    color: #d63384 !important;
    text-align: center;
    font-size: 42px !important;
    font-weight: 700 !important;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    color: #8f3d68;
    font-size: 17px;
    margin-bottom: 30px;
}

.stTextArea label {
    color: #a61e5c !important;
    font-weight: 600;
    font-size: 16px;
}

.stTextArea textarea {
    background-color: #fff8fb !important;
    color: #4a1831 !important;
    border: 2px solid #f783ac !important;
    border-radius: 14px !important;
    padding: 14px !important;
    font-size: 16px !important;
    min-height: 180px;
}

.stTextArea textarea:focus {
    border-color: #d63384 !important;
    box-shadow: 0 0 10px rgba(214, 51, 132, 0.25) !important;
}

.stButton button {
    width: 100%;
    background: linear-gradient(135deg, #d63384, #e85d9e);
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 20px !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    margin-top: 10px;
}

.stButton button:hover {
    background: linear-gradient(135deg, #b52b6f, #d63384);
    color: white !important;
    box-shadow: 0 6px 15px rgba(214, 51, 132, 0.3);
}

.stSuccess {
    background-color: #ffe0ed !important;
    color: #9c245d !important;
    border-radius: 12px !important;
    border: 1px solid #f783ac !important;
}

.stWarning {
    background-color: #fff0f5 !important;
    color: #9c245d !important;
    border-radius: 12px !important;
    border: 1px solid #f5a3c7 !important;
}

.response-box {
    background: rgba(255, 255, 255, 0.75);
    border: 2px solid #f783ac;
    border-radius: 15px;
    padding: 20px;
    margin-top: 20px;
    color: #4a1831;
    box-shadow: 0 5px 15px rgba(214, 51, 132, 0.1);
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Gemini AI Chatbot")

st.markdown(
    '<div class="subtitle">Ask Gemini anything and get an AI-powered response</div>',
    unsafe_allow_html=True
)

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words...."
)

if st.button("Generate Response"):

    if prompt:

        with st.spinner("Gemini is thinking....."):

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

        st.success("Response generated!")

        st.markdown(
            f'<div class="response-box">{response.text}</div>',
            unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a prompt.")