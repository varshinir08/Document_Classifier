import streamlit as st
import requests

# Set up page config
st.set_page_config(page_title="Document Classifier", layout="wide")

# Side Panel for Description
st.sidebar.header("Appian Document Classifier")
st.sidebar.markdown("""
    The **Appian Document Classifier** helps you upload and classify your documents into categories using state-of-the-art AI models.
    
    Supported document types:
    - PDF
    - DOCX
    - TXT
    
    Upload a document to get started with classification.
""")

# Title and Description
st.title("Document Classifier")
st.markdown("### Upload a Document to Classify")
st.markdown("""
    This tool helps you classify documents. Simply upload a document in PDF, DOCX, or TXT format to begin.
""")

# File Upload Section
st.markdown("### Choose a document to upload:")
uploaded_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")
    # Show file size (for feedback)
    st.write(f"File size: {uploaded_file.size / 1024:.2f} KB")

    # Simulate the document classification (button triggers backend)
    if st.button("Classify Document"):
        st.write("Classifying the document... Please wait.")
        response = requests.post("http://127.0.0.1:5000/upload", files={"file": uploaded_file})
        
        if response.status_code == 200:
            st.success("Document classified successfully!")
            st.json(response.json())  # Show the classification results
        else:
            st.error("Failed to classify the document. Please try again.")

