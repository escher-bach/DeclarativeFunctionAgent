from .common import genai, content, json, os

def analyze_arguments(doc_content: dict) -> dict:
    """
    Analyze legal arguments and reasoning in the document.

    Args:
        doc_content: Dictionary containing parsed legal document content

    Returns:
        Dictionary containing analysis of legal arguments
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
                    "analysis": content.Schema(
                        type=content.Type.OBJECT,
                        properties={
                            "key_arguments": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "legal_basis": content.Schema(type=content.Type.STRING),
                            "potential_issues": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "recommendations": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING))
                        }
                    )
                }
            ),
            "response_mime_type": "application/json"
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="Analyze the legal arguments and reasoning in this document. Identify key arguments, legal basis, potential issues, and provide recommendations."
        )

        doc_text = f"Document Type: {doc_content['metadata'].get('Type', 'Unknown')}\n\n"
        doc_text += f"Sections and Clauses:\n"
        for section, section_content in doc_content['sections'].items():
            doc_text += f"\nSection {section}:\n{section_content}"
        for clause, clause_content in doc_content['clauses'].items():
            doc_text += f"\nClause {clause}:\n{clause_content}"

        response = model.generate_content(doc_text)
        
        try:
            result = json.loads(response.text)
            return result.get('analysis', {})
        except json.JSONDecodeError:
            return {"error": "Failed to parse argument analysis results"}

    except Exception as e:
        return {"error": f"Argument analysis failed: {str(e)}"}
