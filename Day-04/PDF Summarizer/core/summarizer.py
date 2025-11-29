from agent.orchestrator import pdf_agent

def get_summary(text: str, summary_type: str) -> str:
    """
    Calls the agent to summarize the provided text using the summarize_text tool.
    """
    prompt = f"Please summarize the following text as a {summary_type} summary: {text}"
    # Assuming pdf_agent.run() will correctly interpret the prompt and use the bound tool.
    response = pdf_agent.run(prompt=prompt)
    # The actual output would need to be parsed from the agent's response.
    # For simplicity, returning the raw response or a placeholder until agent output structure is clear.
    return str(response) # In a real scenario, we'd parse the tool output from response