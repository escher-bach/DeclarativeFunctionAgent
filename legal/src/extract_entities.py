from .common import genai, content, json, os

def extract_entities(doc_content: dict) -> dict:
    """
    Extract entities (people, organizations, dates, locations) from legal documents.

    Args:
        doc_content: Dictionary containing parsed legal document content

    Returns:
        Dictionary containing extracted entities
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
                    "entities": content.Schema(
                        type=content.Type.OBJECT,
                        properties={
                            "people": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "organizations": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "dates": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING)),
                            "locations": content.Schema(type=content.Type.ARRAY, items=content.Schema(type=content.Type.STRING))
                        }
                    )
                }
            ),
            "response_mime_type": "application/json"
        }

        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",
            generation_config=generation_config,
            system_instruction="Extract entities from legal document content. Focus on identifying people, organizations, dates, and locations."
        )

        # Prepare document content for analysis
        doc_text = f"Metadata:\n{json.dumps(doc_content['metadata'], indent=2)}\n\n"
        for section, section_content in doc_content['sections'].items():
            doc_text += f"Section {section}:\n{section_content}\n\n"
        for clause, clause_content in doc_content['clauses'].items():
            doc_text += f"Clause {clause}:\n{clause_content}\n\n"

        response = model.generate_content(doc_text)
        
        try:
            result = json.loads(response.text)
            return result.get('entities', {})
        except json.JSONDecodeError:
            return {"error": "Failed to parse entity extraction results"}

    except Exception as e:
        return {"error": f"Entity extraction failed: {str(e)}"}
