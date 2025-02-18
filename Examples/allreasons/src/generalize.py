from .common import os, genai, content, json

def generalize(patterns: str) -> str:
    """
    Takes identified patterns as input and forms a general hypothesis or rule.

    Args:
        patterns: A string describing the identified patterns.

    Returns:
        A general hypothesis or rule that explains the patterns, or an error message if the process fails.
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
                    "general_hypothesis": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are an expert at forming general hypothesis or rules that describe the patterns.",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"Based on the following patterns, form a general hypothesis or rule:\n{patterns}"
        response = chat_session.send_message(prompt)
        
        try:
            json_output = json.loads(response.text)
            return json_output.get("general_hypothesis", "Error: Could not extract general hypothesis from json.")
        except json.JSONDecodeError:
             return f"Error: Could not decode json. The response is: {response.text}"

    except Exception as e:
      return f"An error occurred: {e}"
