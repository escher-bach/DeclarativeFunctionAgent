from .common import os, genai, content, json

def explains(hypothesis: str, observation: str) -> bool:
    """
    Evaluates whether a given hypothesis adequately explains a set of observations.

    Args:
        hypothesis: The hypothesis to evaluate.
        observation: The observation to check against the hypothesis.

    Returns:
        True if the hypothesis explains the observation, False otherwise, or an error message if the process fails.
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
                    "explains": content.Schema(
                        type=content.Type.BOOLEAN,
                    ),
                    "reason": content.Schema(
                        type=content.Type.STRING,
                    )
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are an expert at determining whether a hypothesis explains an observation. Respond with a JSON object with 'explains' as true if the hypothesis explains the observation, and false otherwise. Provide a 'reason' explaining your decision.",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"Does the following hypothesis explain the observation?\nHypothesis: {hypothesis}\nObservation: {observation}"
        response = chat_session.send_message(prompt)

        try:
            json_output = json.loads(response.text)
            return json_output.get("explains", "Error: Could not extract 'explains' value from json.")
        except json.JSONDecodeError:
             return f"Error: Could not decode json. The response is: {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"
