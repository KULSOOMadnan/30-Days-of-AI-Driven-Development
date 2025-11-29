from agent.orchestrator import pdf_agent

def generate_quiz_content(text: str) -> str:
    """
    Calls the agent to generate a quiz based on the provided text using the generate_quiz tool.
    """
    prompt = f"Please generate a multiple-choice and mixed question quiz based on the following text: {text}"
    # Assuming pdf_agent.run() will correctly interpret the prompt and use the bound tool.
    response = pdf_agent.run(prompt=prompt)
    # The actual output would need to be parsed from the agent's response.
    # For simplicity, returning the raw response or a placeholder until agent output structure is clear.
    return str(response) # In a real scenario, we'd parse the tool output from response
