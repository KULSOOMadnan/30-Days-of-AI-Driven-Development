import streamlit as st
from core.pdf_reader import read_pdf
from core.quiz_generator import generate_quiz_content
from ui.components.history_viewer import add_to_history # Import the helper function

def quiz_viewer():
    st.header("Generate and View Quiz")

    if 'uploaded_pdf_path' in st.session_state and st.session_state['uploaded_pdf_path']:
        pdf_path = st.session_state['uploaded_pdf_path']
        st.write(f"Generating quiz for: {st.session_state['uploaded_pdf_name']}")

        if st.button("Generate Quiz"):
            with st.spinner("Extracting text and generating quiz..."):
                try:
                    text = read_pdf(pdf_path)
                    quiz = generate_quiz_content(text)
                    st.session_state['generated_quiz'] = quiz
                    st.success("Quiz Generated!")
                    # Add to history immediately after generation
                    add_to_history(
                        filename=st.session_state['uploaded_pdf_name'],
                        quiz=quiz
                    )
                except Exception as e:
                    st.error(f"Error generating quiz: {e}")

        if 'generated_quiz' in st.session_state and st.session_state['generated_quiz']:
            st.subheader("Generated Quiz:")
            st.write(st.session_state['generated_quiz'])
            # It's better not to clear here, as user might want to see it until they navigate away.
            # The history entry is already made.
    else:
        st.info("Please upload a PDF file on the 'Upload' page first.")