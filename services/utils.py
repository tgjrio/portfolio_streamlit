import streamlit as st
import pandas as pd
import requests
import json
import uuid
from services.table_style import display_aggrid_table


def initialize_session_state():
    if 'field_transformations' not in st.session_state:
        st.session_state['field_transformations'] = []
    if 'field_creations' not in st.session_state:
        st.session_state['field_creations'] = []

def display_transformations_and_creations():
    st.divider()
    st.subheader("MORPHS SUBMITTED")

    if st.session_state['field_transformations']:
        st.write("**Field Transformations:**")
        for idx, transformation in enumerate(st.session_state['field_transformations'], start=1):
            st.write(f"{idx}. {transformation['instruction']}")

    if st.session_state['field_creations']:
        st.write("**Field Creations:**")
        for idx, creation in enumerate(st.session_state['field_creations'], start=1):
            st.write(f"{idx}. New Field: `{creation['new_field_name']}` with conditions: {creation['condition_instructions']}")

def reset_transformations_and_creations():
    col1, col_spacer, col2 = st.columns([1, 4, 1])

    with col1:
        if st.button("Reset", type="primary"):
            st.session_state['field_transformations'] = []
            st.session_state['field_creations'] = []
            st.success("All instructions have been cleared.")


def process_data(data):
    # Define columns within this function
    col1, col_spacer, col2 = st.columns([1, 4, 1])  # This line is added to ensure col2 is defined
    
    with col1:
        st.subheader("Process Data")
        process_clicked = st.button("Process", icon=":material/bolt:", type="primary")
        print("data", data)

    if process_clicked:
        session_id = str(uuid.uuid4())  # Generate unique session ID

        # Helper function to convert timestamps
        def convert_timestamps(obj):
            if isinstance(obj, pd.Timestamp):
                return obj.strftime("%Y-%m-%d %H:%M:%S")  # Customize the format as needed
            return obj

        # Prepare the data and instructions
        combined_instructions = {
            "field_transformations": st.session_state.get('field_transformations', []),
            "field_creations": st.session_state.get('field_creations', [])
        }
        data = {
            "data": data.map(convert_timestamps).to_dict(orient="records")
        }

        payload = {
            "data": data["data"],
            "instructions": combined_instructions
        }

        st.divider()
        st.subheader("Instructions Sent to API")

        # Make the request to the FastAPI service
        try:
            st.info("Processing data...")
            response = requests.post("http://localhost:8000/process-data/", json=payload)
            if response.status_code == 200:
                result = response.json()

            # Assuming `result["modified_data"]` is what you want to process
            if "modified_data" in result:
                modified_data = result["modified_data"]['data']
                
                # Ensure `modified_data` is a list of dictionaries
                if isinstance(modified_data, list) and all(isinstance(item, dict) for item in modified_data):
                    processed_data = pd.DataFrame(modified_data)
                    st.success("Data processing completed.")
                    st.dataframe(processed_data)  # Display as a Streamlit DataFrame table
                else:
                    st.error("Unexpected data format. Expected a list of dictionaries for 'modified_data'.")
                    st.json(result)  # Display the raw JSON response for inspection
            elif "data" in result:
                # Handling the case where "data" is present
                data = result["data"]
                
                # Ensure `data` is a list of dictionaries
                if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                    processed_data = pd.DataFrame(data)
                    st.success("Data processing completed.")
                    st.dataframe(processed_data)  # Display as a Streamlit DataFrame table
                else:
                    st.error("Unexpected data format. Expected a list of dictionaries for 'data'.")
                    st.json(result)  # Display the raw JSON response for inspection
            else:
                st.error("Unexpected response format. Could not find 'modified_data' or 'data' key.")
                st.json(result)  # Fallback to display the raw JSON response

        except requests.RequestException as e:
            st.error(f"Failed to connect to the API: {e}")

# def process_data(data, gpt_generator):
#     # Define columns within this function
#     col1, col_spacer, col2 = st.columns([1, 4, 1])  # This line is added to ensure col2 is defined
    
#     with col1:
        
#         st.subheader("Process Data")
#         process_clicked = st.button("Process", icon=":material/bolt:", type="primary")

#     if process_clicked:

#         session_id = str(uuid.uuid4())  # Generate unique session ID

#         # Helper function to convert timestamps
#         def convert_timestamps(obj):
#             if isinstance(obj, pd.Timestamp):
#                 return obj.strftime("%Y-%m-%d %H:%M:%S")  # Customize the format as needed
#             return obj

#         combined_instructions = {
#             "field_transformations": st.session_state.get('field_transformations', []),
#             "field_creations": st.session_state.get('field_creations', [])
#         }
#         data = {
#             "data": data.map(convert_timestamps).to_dict(orient="records") 
#         }

#         instructions_json = json.dumps(combined_instructions, indent=4)
#         st.divider()
#         st.subheader("Instructions Sent to AI")

#         # AI-1: Convert Schema Fields per Instructions
#         st.info("Processing data...")
#         schema_result = gpt_generator.generate_response(
#             session_id=session_id,
#             instructions=f"Make the updates to the data using the given instructions for field_transformations and field_creations: {instructions_json}. Your response should only be in JSON format; do not wrap in ```json markdown.",
#             data=data
#         )
#         st.success("Data processing initiated.")

#         # Display the schema result (assuming this returns a DataFrame or a compatible object)
#         try:
#             # Convert the string response into a Python dictionary
#             schema_result_dict = json.loads(schema_result)
            
#             # Extract the 'data' key, assuming it contains the list of dictionaries
#             if "data" in schema_result_dict and isinstance(schema_result_dict["data"], list):
#                 processed_data = pd.DataFrame(schema_result_dict["data"])
#                 display_aggrid_table(processed_data)  # Display as AgGrid table
#             else:
#                 st.error("Unexpected response format. Could not find 'data' key.")
#                 st.json(schema_result_dict)  # Fallback to display the raw JSON response
#         except json.JSONDecodeError:
#             st.error("Failed to decode the AI response as JSON.")
#             st.write(f"Raw Response: {schema_result}")