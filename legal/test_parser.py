from src.parse_legal_documents import parse_legal_documents
import os
import json

def main():
    # Get the absolute path to the samples directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    samples_dir = os.path.join(current_dir, 'samples')
    
    # Get all .txt files from samples directory
    document_paths = tuple(
        os.path.join(samples_dir, f) 
        for f in os.listdir(samples_dir) 
        if f.endswith('.txt')
    )
    
    try:
        # Parse the documents
        parsed_docs = parse_legal_documents(document_paths)
        
        # Print the results in a structured way
        for path, content in parsed_docs.items():
            print(f"\nDocument: {os.path.basename(path)}")
            print("=" * 60)
            
            print("\nMetadata:")
            print("-" * 20)
            for key, value in content['metadata'].items():
                print(f"{key}: {value}")
            
            print("\nSections:")
            print("-" * 20)
            for section, text in content['sections'].items():
                print(f"\n{section}:")
                print(f"{text}")
            
            print("\nClauses:")
            print("-" * 20)
            for clause, text in content['clauses'].items():
                print(f"\n{clause}:")
                print(f"{text}")
            
            print("\n" + "=" * 60)
            
        # Save parsed output to JSON for reference
        output_file = os.path.join(current_dir, 'parsed_output.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(parsed_docs, f, indent=2)
        print(f"\nParsed output saved to: {output_file}")

    except Exception as e:
        print(f"Error processing documents: {e}")

if __name__ == "__main__":
    main()