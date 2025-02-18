from .common import os, genai, content, json

def transfer_knowledge(source: str, mapping: dict) -> str:
    """
    Transfers knowledge from the source text to a target concept based on the provided mapping.

    Args:
        source: The source text containing the knowledge.
        mapping: A dictionary representing the correspondences between concepts in the source and target domains.
                 Example: {"bird": "airplane", "wings": "wings", "fly": "flight"}

    Returns:
        A string explaining the target concept using the knowledge transferred from the source,
        or an error message if the process fails.
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
                    "transferred_knowledge": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="You are an expert at transferring knowledge from one concept to another based on a provided mapping. Explain the target concept using knowledge from the source, guided by the mapping.",
        )

        chat_session = model.start_chat(
            history=[],
        )

        prompt = f"Source text: {source}\nMapping: {mapping}\n\nExplain the target concept, transferring knowledge from the source based on the mapping."
        response = chat_session.send_message(prompt)

        try:
            json_output = json.loads(response.text)
            return json_output.get("transferred_knowledge", "Error: Could not extract transferred knowledge from json.")
        except json.JSONDecodeError:
            return f"Error: Could not decode json. The response is: {response.text}"


    except Exception as e:
        return f"An error occurred: {e}"
