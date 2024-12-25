import streamlit as st
import requests

# Upload multiple files
uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

# If files are uploaded, send them to Flask server
if uploaded_files:
    files = {}  # Empty dictionary to store the files

    # Loop through the uploaded files and prepare them for sending
    for idx, file in enumerate(uploaded_files):
        files[f'file{idx}'] = file.getvalue()  # Get the content of the file

    # Send the files to Flask using a POST request
    response = requests.post('http://127.0.0.1:5000/upload', files=files)

    # Show the response from the server
    st.write(response.json())
