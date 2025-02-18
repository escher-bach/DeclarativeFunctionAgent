from .common import genai, content, json, os

def extract_key_facts(doc_content: dict) -> dict:
    """
    Extract key facts from legal documents.

    Args:
        doc_content: Dictionary containing parsed legal document content

    Returns:
        Dictionary containing key facts
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
                    "key_facts": content.Schema(
                        type=content.Type.OBJECT,
                        properties={
                            "parties": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "obligations": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "dates": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "terms": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING))
                        }
                    )
                }
            ),
            "response_mime_type": "application/json"
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="Extract key facts from the legal document, focusing on parties involved, obligations, important dates, and key terms."
        )

        # Prepare document content
        doc_text = f"Metadata:\n{json.dumps(doc_content['metadata'], indent=2)}\n\n"
        doc_text += "Document Content:\n"
        for section, section_content in doc_content['sections'].items():
            doc_text += f"\nSection {section}:\n{section_content}"
        for clause, clause_content in doc_content['clauses'].items():
            doc_text += f"\nClause {clause}:\n{clause_content}"

        response = model.generate_content(doc_text)
        
        try:
            result = json.loads(response.text)
            return result.get('key_facts', {})
        except json.JSONDecodeError:
            return {"error": "Failed to parse key facts extraction results"}

    except Exception as e:
        return {"error": f"Key facts extraction failed: {str(e)}"}
