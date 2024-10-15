import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


# Define a function to get a response from OpenAI
def get_openai_response(query):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None:
        st.error("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
        return "OpenAI API key is missing."

    openai.api_key = openai_api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=query,
        temperature=0.5,
        max_tokens=150
    )
    return response.choices[0].text.strip()


# Set Streamlit page configuration
st.set_page_config(page_title="OpenAI ChatBot", page_icon=":earth_americas:", layout="wide")

# Streamlit app header
st.header("OpenAI ChatBot")

# Text input field for the user query
user_query = st.text_input("Enter your query here", key="input")

# Submit button
submit = st.button("Submit")

# Generate and display the response when the button is pressed
if submit:
    response = get_openai_response(user_query)
    st.write(response)
