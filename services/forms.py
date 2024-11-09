import streamlit as st



def field_transformations():
    st.subheader("STEP 2: FIELD TRANSFORMATIONS")
    
    # Form for field name transformation instructions
    with st.form(key='field_transformation_form', clear_on_submit=True):
        field_instructions = st.text_area(
            "Provide field name instructions (e.g., rename 'salary' to 'annual_income', capitalize 'country' values, etc.)"
        )
        submit_field_transformation = st.form_submit_button("Submit", type='primary')
        
        if submit_field_transformation:
            if len(st.session_state['field_transformations']) >= 3:
                st.error("You can only create up to 3 field transformation instructions.")
            elif field_instructions:
                st.session_state['field_transformations'].append({"instruction": field_instructions})
                st.success("Field transformation added.")
            else:
                st.warning("Please enter an instruction before submitting.")


def create_new_fields():
    st.subheader("STEP 3: CREATE NEW FIELDS")

    # Form for creating new fields based on conditions
    with st.form(key='new_field_creation_form', clear_on_submit=True):
        new_field_name = st.text_input("New Field Name")
        condition_instructions = st.text_area(
            "Enter the conditions for creating the new field (e.g., 'If salary > 80000 then High, else Medium or Low')."
        )
        submit_new_field = st.form_submit_button("Submit", type='primary')
        
        if submit_new_field:
            if len(st.session_state['field_creations']) >= 3:
                st.error("You can only create up to 3 new fields.")
            elif new_field_name and condition_instructions:
                st.session_state['field_creations'].append({
                    "new_field_name": new_field_name,
                    "condition_instructions": condition_instructions
                })
                st.success(f"New field '{new_field_name}' creation instructions added.")
            else:
                st.warning("Please enter both a new field name and condition instructions before submitting.")