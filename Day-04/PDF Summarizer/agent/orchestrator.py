from agents import Agent, OpenaiChatCompletionModel
from agent.tools import extract_pdf_text, summarize_text, generate_quiz

# Initialize the Gemini model
llm = OpenaiChatCompletionModel(model="gemini-2.0-flash", base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# Define the PDF Summarizer & Quiz Generator agent
pdf_agent = Agent(
    name="PDF_Summarizer_Quiz_Generator",
    instructions="You are a PDF Summarizer & Quiz Generator. Always base your output strictly on the extracted PDF text.",
    tools=[extract_pdf_text, summarize_text, generate_quiz],
    llm=llm
)
