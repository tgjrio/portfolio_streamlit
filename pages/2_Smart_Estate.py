import streamlit as st
import requests
import json


# Define the FastAPI endpoint URL
API_URL = "https://transformation-ai-service-834521154069.us-east1.run.app/process_query/"


st.title("Query Assistant using BigQuery and OpenAI")
st.write("Enter a query to generate and execute SQL queries using AI:")

# Text input for user queries
user_input = st.text_input("Your Query", "")

# Process the query when the button is pressed
if st.button("Submit"):
    if user_input:
        # Send the request to the FastAPI endpoint
        with st.spinner("Processing..."):
            try:
                response = requests.post(API_URL, json={"user_input": user_input})
                if response.status_code == 200:
                    response_data = response.json()
                    query = response_data.get("query", "")
                    ai_response = response_data.get("response", "")
                    # print(response_data)
                    st.subheader("Generated SQL Query")
                    st.markdown(query)

                    st.subheader("AI Response")
                    st.json(response_data)
                    st.markdown(ai_response, unsafe_allow_html=True)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a query.")