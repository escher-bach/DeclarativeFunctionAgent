from .common import genai, content, json, os

def summarize_case(doc_content: dict) -> dict:
    """
    Generate a comprehensive summary of the legal document.

    Args:
        doc_content: Dictionary containing parsed legal document content

    Returns:
        Dictionary containing document summary
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
                    "summary": content.Schema(
                        type=content.Type.OBJECT,
                        properties={
                            "brief": content.Schema(type=content.Type.STRING),
                            "key_points": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "obligations": content.Schema(type=content.Type.OBJECT, properties={
                                "party1": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                                "party2": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING))
                            }),
                            "risk_assessment": content.Schema(type=content.Type.STRING)
                        }
                    )
                }
            ),
            "response_mime_type": "application/json"
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="Generate a comprehensive summary of the legal document, including key points, obligations of each party, and risk assessment."
        )

        # Prepare document content
        doc_text = f"Document Type: {doc_content['metadata'].get('Type', 'Unknown')}\n\n"
        doc_text += f"Contract Details:\n{json.dumps(doc_content['metadata'], indent=2)}\n\n"
        doc_text += "Document Content:\n"
        for section, section_content in doc_content['sections'].items():
            doc_text += f"\nSection {section}:\n{section_content}"
        for clause, clause_content in doc_content['clauses'].items():
            doc_text += f"\nClause {clause}:\n{clause_content}"

        response = model.generate_content(doc_text)
        
        try:
            result = json.loads(response.text)
            return result.get('summary', {})
        except json.JSONDecodeError:
            return {"error": "Failed to parse document summary results"}

    except Exception as e:
        return {"error": f"Document summarization failed: {str(e)}"}
