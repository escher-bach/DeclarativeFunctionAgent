from .common import os, genai, content, json

def find_correspondences(source: str, target: str) -> str:
    """
    Identifies similarities and relationships between two input strings.

    Args:
        source: The source string.
        target: The target string.

    Returns:
        A string containing the identified correspondences, or an error message if the process fails.
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
                    "correspondences": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are an expert in finding semantic correspondences between two texts. Identify the similarities and relationships between the two texts as detailed as possible",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"Identify the correspondences between the following two texts:\nSource: {source}\nTarget: {target}"
        response = chat_session.send_message(prompt)

        try:
            json_output = json.loads(response.text)
            return json_output.get("correspondences", "Error: Could not extract correspondences from json.")
        except json.JSONDecodeError:
             return f"Error: Could not decode json. The response is: {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"
