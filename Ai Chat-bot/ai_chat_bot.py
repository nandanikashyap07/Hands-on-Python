import streamlit as st
import google.generativeai as genai


key = "ENTER YOUR KEY HERE"
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash")


st.set_page_config(page_title="Gemini ChatBot", layout="centered")
st.title("🤖 Gemini ChatBot using Streamlit")
st.write("Ask anything! Type your query below:")


user_input = st.text_input("Enter your question")


if st.button("Generate Response"):
    if user_input.strip() != "":
        response = model.generate_content(user_input)
        st.subheader("🔹 BOT Response:")
        st.write(response.text)
    else:
        st.warning("Please enter a valid query!")
