import os
from src.common import genai, content, json

# Import implemented functions
from src.parse_legal_documents import parse_legal_documents
from src.extract_entities import extract_entities
from src.summarize_case import summarize_case
from src.identify_legal_claims import identify_legal_claims
from src.extract_key_facts import extract_key_facts
from src.analyze_arguments import analyze_arguments
from src.pretty_legal_formatter import format_legal_analysis

# Original implementation
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
    argument_analysis = analyze_arguments(parsed_docs)
    
    analysis_report = {
        'summary': case_summary,
        'claims': legal_claims,
        'facts': key_facts,
        'arguments': argument_analysis,
        'entities': key_entities
    }
    
    return analysis_report

def process_legal_documents():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    samples_dir = os.path.join(current_dir, 'samples')
    output_dir = os.path.join(current_dir, 'output')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get all .txt files from samples directory
    document_paths = tuple(
        os.path.join(samples_dir, f) 
        for f in os.listdir(samples_dir) 
        if f.endswith('.txt')
    )
    
    try:
        # Parse documents
        parsed_docs = parse_legal_documents(document_paths)
        
        results = {}
        for path, doc_content in parsed_docs.items():
            doc_name = os.path.basename(path)
            results[doc_name] = {
                'parsed_structure': doc_content,
                'entities': extract_entities(doc_content),
                'key_facts': extract_key_facts(doc_content),
                'legal_claims': identify_legal_claims(doc_content),
                'analysis': analyze_arguments(doc_content),
                'summary': summarize_case(doc_content)
            }
        
        # Generate pretty formatted output
        formatted_output = os.path.join(output_dir, 'analysis_report.txt')
        format_legal_analysis(results, formatted_output)
        print(f"\nDetailed analysis report has been saved to: {formatted_output}")
        
        return results
    
    except Exception as e:
        print(f"Error processing documents: {e}")
        return None

if __name__ == "__main__":
    results = process_legal_documents()
    if results:
        print("\nProcessing complete! Check the output directory for the formatted report.")
