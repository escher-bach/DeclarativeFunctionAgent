def legal_analyzer(case_documents):
    """
    Args:
        case_documents: str - Legal document text
    
    Returns:
        dict - Complete analysis results
    """
    parsed_docs = parse_legal_documents(case_documents)
    key_entities = extract_entities(parsed_docs)
    
    case_summary = summarize_case(parsed_docs)
    legal_claims = identify_legal_claims(parsed_docs)
    key_facts = extract_key_facts(parsed_docs)
    argument_analysis = analyze_arguments(parsed_docs, legal_claims)
    
    analysis_report = {
        'summary': case_summary,
        'claims': legal_claims,
        'facts': key_facts,
        'arguments': argument_analysis,
        'entities': key_entities
    }
    
    return analysis_report
