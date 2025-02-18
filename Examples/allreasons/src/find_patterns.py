from .common import os, genai, content, json

def find_patterns(observations: str) -> str:
    """
    Analyzes a set of observations to identify recurring patterns or relationships.

    Args:
        observations: A string containing the set of observations.

    Returns:
        A string representing the identified patterns, or an error message if the process fails.
    """
    try:
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_schema": content.Schema(
                type=content.Type.OBJECT,
                properties={
                    "identified_patterns": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are an expert at identifying patterns and relationships in data.",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"Analyze the following observations and identify any recurring patterns or relationships:\n{observations}"
        response = chat_session.send_message(prompt)
        
        try:
            json_output = json.loads(response.text)
            return json_output.get("identified_patterns", "Error: Could not extract identified patterns from json.")
        except json.JSONDecodeError:
             return f"Error: Could not decode json. The response is: {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"
