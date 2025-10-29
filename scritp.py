from google import genai
import streamlit as st

client = genai.Client(api_key='AIzaSyB5dJSLcOxgxEqN3xmXSdbc0kVTi6DfzbY')

st.title("Talk to Agent")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models._generate_images(
            model='gemini-2.0-flash', contents=user_input
        )
    st.write(response.text)
