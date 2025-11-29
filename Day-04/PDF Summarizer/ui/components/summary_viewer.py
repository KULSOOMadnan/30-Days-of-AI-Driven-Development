import streamlit as st
from core.pdf_reader import read_pdf
from core.summarizer import get_summary
from ui.components.history_viewer import add_to_history # Import the helper function

def summary_viewer():
    st.header("View Document Summary")

    if 'uploaded_pdf_path' in st.session_state and st.session_state['uploaded_pdf_path']:
        pdf_path = st.session_state['uploaded_pdf_path']
        st.write(f"Summarizing: {st.session_state['uploaded_pdf_name']}")

        summary_type = st.radio(
            "Select Summary Type:",
            ("short", "medium", "detailed"),
            key="summary_type_radio"
        )

        if st.button("Generate Summary"):
            with st.spinner("Extracting text and generating summary..."):
                try:
                    text = read_pdf(pdf_path)
                    summary = get_summary(text, summary_type)
                    st.session_state['generated_summary'] = summary
                    st.session_state['last_summary_type'] = summary_type
                    st.success("Summary Generated!")
                    # Add to history immediately after generation
                    add_to_history(
                        filename=st.session_state['uploaded_pdf_name'],
                        summary_type=summary_type,
                        summary=summary
                    )
                except Exception as e:
                    st.error(f"Error generating summary: {e}")

        if 'generated_summary' in st.session_state and st.session_state['generated_summary']:
            st.subheader(f"Generated {st.session_state['last_summary_type']} Summary:")
            st.write(st.session_state['generated_summary'])
            # It's better not to clear here, as user might want to see it until they navigate away.
            # The history entry is already made.
    else:
        st.info("Please upload a PDF file on the 'Upload' page first.")