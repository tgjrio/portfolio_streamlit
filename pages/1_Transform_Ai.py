from services.utils import initialize_session_state
from services.data_service import upload_data
from services.forms import field_transformations, create_new_fields
from services.table_style import display_aggrid_table
from services.utils import display_transformations_and_creations, reset_transformations_and_creations, process_data
from services.gpt_service import GPTGenerator
from configs import settings
import streamlit as st

gpt = GPTGenerator(settings.OPENAI_CLIENT)

st.set_page_config(
    page_title="Data Morphing with AI",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize session state
initialize_session_state()

st.title("TRANSFORM DATA WITH AI")
st.divider()
# Introduction
st.markdown(
    """
DataMorph is an AI-powered tool designed to streamline data transformation workflows. By leveraging advanced AI models, it can automatically rename fields, restructure datasets, generate new fields based on custom conditions, and more—all tailored to your specific instructions. With DataMorph, you can focus more on insights and decision-making while reducing the time spent on manual data manipulation.

Simply upload your data, provide your transformation instructions, and let DataMorph handle the rest. Whether you’re preparing datasets for analysis, creating custom reports, or integrating data from multiple sources, DataMorph empowers you to transform your data efficiently and accurately.
    """
)
st.markdown(
    """
    No Data?
     
    Grab a mock file from [Mockaroo](https://www.mockaroo.com/). They offer a free service to generate test data for your projects, so use this if you don't have a file to upload.
    """
)
st.divider()
# Step 1: Upload Data
data = upload_data()
if data is not None:
    display_aggrid_table(data)  # Display data if it is valid

    # Step 2: Field Transformations
    field_transformations()

    # Step 3: Create New Fields
    create_new_fields()

        # Display transformations and creations
    display_transformations_and_creations()

    # Reset button logic
    reset_transformations_and_creations()

    st.divider()

    # Process data
    process_data(data)
    