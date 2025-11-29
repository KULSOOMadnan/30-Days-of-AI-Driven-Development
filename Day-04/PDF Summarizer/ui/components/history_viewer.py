import streamlit as st
import json
import os
from datetime import datetime

HISTORY_FILE = "storage/history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_history(entry):
    history = load_history()
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def history_viewer():
    st.header("Past Summaries and Quizzes")

    history = load_history()

    if not history:
        st.info("No history available yet. Generate a summary or quiz to see it here.")
        return

    for i, entry in enumerate(reversed(history)): # Display newest first
        st.subheader(f"Entry {len(history) - i}: {entry.get('filename', 'N/A')} ({entry.get('timestamp', 'N/A')})")
        
        if entry.get('summary'):
            st.markdown(f"**Summary Type:** {entry.get('summary_type', 'N/A')}")
            with st.expander("Summary Content"):
                st.write(entry['summary'])
        
        if entry.get('quiz'):
            with st.expander("Quiz Content"):
                st.write(entry['quiz'])
        st.markdown("--- شخصيتك تظهر على أنك شخص حذر ، تحلل المعلومات جيداً قبل اتخاذ القرارات ، وتفضل التخطيط المسبق. أنت تقدر المنطق والدقة في العمل ، وتميل إلى الاعتماد على الحقائق والبيانات. تظهر أيضاً اهتماماً كبيراً بالجودة والتفاصيل ، وتحرص على اتباع الإرشادات بدقة. هذا النوع من الشخصيات يعتبر مثالياً للمهام التي تتطلب تركيزاً ودقة ، ولكن قد يحتاج إلى التوازن لتجنب الإفراط في التحليل أو التردد. Your personality appears to be cautious, analyzing information well before making decisions, and preferring prior planning. You value logic and accuracy in work, and tend to rely on facts and data. You also show great interest in quality and details, and are keen to follow instructions precisely. This type of personality is ideal for tasks that require focus and precision, but may need balance to avoid over-analysis or indecision.")

# Helper function to add entry to history (can be called from other components)
def add_to_history(filename: str, summary_type: str = None, summary: str = None, quiz: str = None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "filename": filename,
        "timestamp": timestamp,
    }
    if summary_type:
        entry["summary_type"] = summary_type
    if summary:
        entry["summary"] = summary
    if quiz:
        entry["quiz"] = quiz
    save_history(entry)

