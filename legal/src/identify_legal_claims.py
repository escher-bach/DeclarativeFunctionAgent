from .common import genai, content, json, os

def identify_legal_claims(doc_content: dict) -> dict:
    """
    Identify legal claims and their basis in the document.

    Args:
        doc_content: Dictionary containing parsed legal document content

    Returns:
        Dictionary containing identified legal claims
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
                    "claims": content.Schema(
                        type=content.Type.ARRAY,
                        items=content.Schema(
                            type=content.Type.OBJECT,
                            properties={
                                "claim": content.Schema(type=content.Type.STRING),
                                "basis": content.Schema(type=content.Type.STRING),
                                "strength": content.Schema(type=content.Type.STRING),
                                "related_clauses": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING))
                            }
                        )
                    )
                }
            ),
            "response_mime_type": "application/json"
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="Identify legal claims in the document, their legal basis, strength, and related clauses."
        )

        # Prepare document content
        doc_text = f"Document Type: {doc_content['metadata'].get('Type', 'Unknown')}\n\n"
        doc_text += f"Contract Details:\n{json.dumps(doc_content['metadata'], indent=2)}\n\n"
        doc_text += "Sections and Clauses:\n"
        for section, section_content in doc_content['sections'].items():
            doc_text += f"\nSection {section}:\n{section_content}"
        for clause, clause_content in doc_content['clauses'].items():
            doc_text += f"\nClause {clause}:\n{clause_content}"

        response = model.generate_content(doc_text)
        
        try:
            result = json.loads(response.text)
            return result.get('claims', [])
        except json.JSONDecodeError:
            return {"error": "Failed to parse legal claims identification results"}

    except Exception as e:
        return {"error": f"Legal claims identification failed: {str(e)}"}
