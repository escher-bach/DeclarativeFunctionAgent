# legal

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export GEMINI_API_KEY='your_api_key_here'
```

## Project Structure

- `src/`: Contains individual function implementations
- `main.py`: Main program that uses the implemented functions
- `requirements.txt`: Project dependencies

## Available Functions

### parse_legal_documents
This function takes a string of legal documents and converts them into a structured format that can be easily processed. Example: converting unstructured text to a structured dictionary.

### extract_entities
This function identifies and extracts key entities (e.g., people, organizations, locations) from parsed legal documents. Requires Named Entity Recognition (NER). For example, extracting all company names, involved parties, and dates from a legal case.

### summarize_case
This function generates a concise summary of the legal case from the parsed documents. This requires natural language understanding and summarization capabilities. For example, reducing a lengthy court transcript into a short, informative summary.

### identify_legal_claims
This function identifies and classifies the legal claims being made in the case based on the parsed documents. Requires an understanding of legal terminology and reasoning, making it better suited for human/NLP tools. For example, determining whether a document describes a claim of 'breach of contract' or 'negligence'.

### extract_key_facts
This function extracts the most important facts from the parsed legal documents, focusing on information relevant to the legal claims. Requires judgement about the document. For example, extracting key dates, events, and amounts that are central to the case.

### analyze_arguments
This function analyzes the arguments presented in the legal documents, relating them to the identified legal claims and extracted facts. This requires understanding of legal reasoning and argumentation. For example, identifying the plaintiff's and defendant's arguments and assessing their strengths and weaknesses.

