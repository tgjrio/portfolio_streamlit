import streamlit as st

# Profile picture URL
profile_picture_url = "https://example.com/your-profile-picture.jpg"  # Replace with your image URL

# Custom HTML and CSS for layout
st.markdown(f"""
    <style>
        .profile-card {{
            display: flex;
            flex-direction: row;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 1000px;
            margin: auto;
            padding: 20px;
            height: 800px;
        }}
        .left-section {{
            flex: 1;
            text-align: center;
        }}
        .right-section {{
            flex: 2;
            padding-left: 20px;
        }}
        .profile-picture {{
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
        }}
        .contact-info {{
            margin-top: 15px;
            text-align: left;
        }}
        .contact-info p {{
            margin: 5px 0;
            color: #2c3e50;
            font-size: 1em;
        }}
        .title {{
            font-size: 2em;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .section-title {{
            font-size: 1.5em;
            color: #34495e;
            margin-top: 20px;
        }}
        .progress-bar-container {{
            margin-top: 10px;
        }}
        .progress-bar {{
            background-color: #e0e0e0;
            border-radius: 5px;
            overflow: hidden;
            margin-bottom: 10px;
        }}
        .progress-bar-fill {{
            height: 20px;
            border-radius: 5px;
            text-align: right;
            padding-right: 5px;
            line-height: 20px;
            color: white;
            font-weight: bold;
        }}
        .progress-bar-fill.tools {{
            background-color: #3498db;
        }}
        .progress-bar-fill.languages {{
            background-color: #e74c3c;
        }}
    </style>
    
    <div class="profile-card">
        <div class="left-section">
            <img src="{profile_picture_url}" class="profile-picture" alt="Profile Picture">
            <div class="contact-info">
                <p><strong>Email:</strong> your.email@example.com</p>
                <p><strong>Phone:</strong> (123) 456-7890</p>
                <p><strong>Location:</strong> City, Country</p>
            </div>
        </div>
        <div class="right-section">
            <div class="title">Data Engineer</div>
            <div class="section-title">Tools Expertise</div>
            <div class="progress-bar-container">
                <div class="progress-bar">
                    <div class="progress-bar-fill tools" style="width: 90%;">90%</div>
                </div>
                <div class="progress-bar">
                    <div class="progress-bar-fill tools" style="width: 80%;">80%</div>
                </div>
                <!-- Add more tools as needed -->
            </div>
            <div class="section-title">Programming Languages</div>
            <div class="progress-bar-container">
                <div class="progress-bar">
                    <div class="progress-bar-fill languages" style="width: 85%;">85%</div>
                </div>
                <div class="progress-bar">
                    <div class="progress-bar-fill languages" style="width: 75%;">75%</div>
                </div>
                <!-- Add more languages as needed -->
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)