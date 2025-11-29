import streamlit as st
import os
from dotenv import load_dotenv

from ui.components.uploader import pdf_uploader
from ui.components.summary_viewer import summary_viewer
from ui.components.quiz_viewer import quiz_viewer
from ui.components.history_viewer import history_viewer

# Load environment variables
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="PDF Summarizer & Quiz Generator")

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Upload", "Summary", "Quiz", "History"])

    if selection == "Upload":
        st.title("Upload PDF")
        pdf_uploader()
    elif selection == "Summary":
        st.title("Summary Viewer")
        summary_viewer()
    elif selection == "Quiz":
        st.title("Quiz Generator")
        quiz_viewer()
    elif selection == "History":
        st.title("History Viewer")
        history_viewer()

if __name__ == "__main__":
    main()
