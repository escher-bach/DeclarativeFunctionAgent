from .common import os, genai, content, json

def is_most_plausible(statements: list[str]) -> str:
    """
    Assesses the plausibility of a set of statements and returns the most plausible one.

    Args:
        statements: A list of statements to evaluate.

    Returns:
        The most plausible statement from the list, or an error message if the process fails.
    """
    try:
        generation_config = {
            "temperature": 0.5,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_schema": content.Schema(
                type=content.Type.OBJECT,
                properties={
                    "most_plausible_statement": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "reasoning": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are an expert at determining the most plausible statement from a list of statements.",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"From the following statements, identify the most plausible one and provide a brief explanation:\n"
        for i, statement in enumerate(statements):
            prompt += f"{i+1}. {statement}\n"

        response = chat_session.send_message(prompt)

        try:
            json_output = json.loads(response.text)
            return json_output.get("most_plausible_statement", "Error: Could not extract the most plausible statement from json.")
        except json.JSONDecodeError:
            return f"Error: Could not decode json. The response is: {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"
