from .common import os, genai, content, json

def generate_joke(topic: str) -> str:
    """
    Generates a joke related to the given topic.

    Args:
        topic: The topic for the joke.

    Returns:
        A joke related to the topic, or an error message if joke generation fails.
    """
    try:
        generation_config = {
            "temperature": 0.8,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_schema": content.Schema(
                type=content.Type.OBJECT,
                properties={
                    "joke": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are a professional comedian, skilled at generating jokes related to any topic. Always provide a clean joke that can be said in a public.",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"Generate a joke about {topic}."
        response = chat_session.send_message(prompt)

        try:
            json_output = json.loads(response.text)
            return json_output.get("joke", "Error: Could not extract joke from json.")
        except json.JSONDecodeError:
            return f"Error: Could not decode json. The response is: {response.text}"


    except Exception as e:
        return f"An error occurred: {e}"
