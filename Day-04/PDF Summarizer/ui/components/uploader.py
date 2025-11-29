import streamlit as st
import os

def pdf_uploader():
    st.header("Upload your PDF document")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # To save the uploaded file temporarily
        file_path = os.path.join("storage", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        st.session_state['uploaded_pdf_path'] = file_path
        st.session_state['uploaded_pdf_name'] = uploaded_file.name
    else:
        st.session_state['uploaded_pdf_path'] = None
        st.session_state['uploaded_pdf_name'] = None

    return st.session_state.get('uploaded_pdf_path')
