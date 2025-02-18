from .common import os, genai, content, json

def synthesis(thesis: str, antithesis: str) -> str:
    """
    Synthesizes a thesis and its antithesis into a new statement.

    Args:
        thesis: The initial statement.
        antithesis: The opposing statement.

    Returns:
        A synthesized statement, or an error message if the synthesis fails.
    """

    try:
        # Define the generation config with the desired output schema
        generation_config = {
            "temperature": 0.7, # Adjusted temperature for more consistent synthesis
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
             "response_schema": content.Schema(
                type=content.Type.OBJECT,
                properties={
                    "synthesis_statement": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
             ),
            "response_mime_type": "application/json",

        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp", # Or your preferred model
            generation_config=generation_config,
            system_instruction="You are an expert in generating synthesis between a thesis and antithesis statement",
        )

        chat_session = model.start_chat(
           history=[ ]
        )
        prompt = f"Synthesize the following statements into a single, coherent statement:\nThesis: {thesis}\nAntithesis: {antithesis}"
        response = chat_session.send_message(prompt)

        # Attempt to parse the JSON response
        try:
            json_output = json.loads(response.text)
            return json_output.get("synthesis_statement", "Error: Could not extract synthesis statement from json.")
        except json.JSONDecodeError:
            return f"Error: Could not decode json. The response is: {response.text}"

    except Exception as e:
      return f"An error occurred: {e}"
