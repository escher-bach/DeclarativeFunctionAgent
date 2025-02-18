def parse_legal_documents(document_paths):
    """
    Parses legal documents into a structured format.

    Args:
        document_paths (tuple): A tuple containing file paths to legal document text files.

    Returns:
        dict: A dictionary with document structure:
            {
                'file_path': {
                    'metadata': {
                        'Contract': str,
                        'Date': str,
                        'Parties': str,
                        'Type': str
                    },
                    'sections': {
                        'section_name': 'section_content'
                    },
                    'clauses': {
                        'clause_name': 'clause_content'
                    }
                }
            }

    Raises:
        TypeError: If input is not a tuple or paths are not strings
        FileNotFoundError: If a document file cannot be found
    """
    import re
    import os

    if not isinstance(document_paths, tuple):
        raise TypeError("Input must be a tuple of file paths.")

    parsed_documents = {}

    for path in document_paths:
        if not isinstance(path, str):
            raise TypeError("Each path must be a string.")

        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")

        try:
            with open(path, 'r', encoding='utf-8') as file:
                legal_text = file.read()

            # Initialize document structure
            doc_structure = {
                'metadata': {},
                'sections': {},
                'clauses': {}
            }

            current_section = None
            current_content = []

            for line in legal_text.splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Parse metadata (Contract, Date, Parties, Type)
                metadata_match = re.match(r"([A-Za-z]+):\s*(.*)", line)
                if metadata_match and not (line.startswith('Section:') or line.startswith('Clause:')):
                    key = metadata_match.group(1).strip()
                    value = metadata_match.group(2).strip()
                    doc_structure['metadata'][key] = value
                    continue

                # Parse Sections
                section_match = re.match(r"Section:\s*(.*)", line)
                if section_match:
                    if current_section and current_content:
                        # Save previous section content
                        if current_section.startswith('Section:'):
                            doc_structure['sections'][current_section[8:].strip()] = ' '.join(current_content)
                        elif current_section.startswith('Clause:'):
                            doc_structure['clauses'][current_section[7:].strip()] = ' '.join(current_content)
                    current_section = section_match.group(0)
                    current_content = []
                    continue

                # Parse Clauses
                clause_match = re.match(r"Clause:\s*(.*)", line)
                if clause_match:
                    if current_section and current_content:
                        # Save previous section/clause content
                        if current_section.startswith('Section:'):
                            doc_structure['sections'][current_section[8:].strip()] = ' '.join(current_content)
                        elif current_section.startswith('Clause:'):
                            doc_structure['clauses'][current_section[7:].strip()] = ' '.join(current_content)
                    current_section = clause_match.group(0)
                    current_content = []
                    continue

                # Accumulate content
                if current_section:
                    current_content.append(line)

            # Save the last section/clause
            if current_section and current_content:
                if current_section.startswith('Section:'):
                    doc_structure['sections'][current_section[8:].strip()] = ' '.join(current_content)
                elif current_section.startswith('Clause:'):
                    doc_structure['clauses'][current_section[7:].strip()] = ' '.join(current_content)

            parsed_documents[path] = doc_structure

        except Exception as e:
            raise Exception(f"Error parsing document {path}: {str(e)}")

    return parsed_documents
