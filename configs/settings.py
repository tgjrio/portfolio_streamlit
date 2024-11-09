from openai import OpenAI
import streamlit as st

OPENAI_API_KEY = st.secrets["api_keys"]["OPEN_AI_TOKEN"]
OPENAI_CLIENT = OpenAI(api_key=OPENAI_API_KEY)

PROJECT_ID = st.secrets['gcp_configs']["PROJECT_ID"]
GCS_BUCKET = "test"