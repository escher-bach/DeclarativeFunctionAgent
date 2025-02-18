# dialectic

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

### satisfied
This function takes a statement (thesis) and evaluates if it is considered 'satisfactory' based on some criteria. It may involve complex reasoning or human judgement, making it better suited for human/NLP tools. For example, satisfied('The sky is blue.') could return True if this statement is considered a sufficient answer, or False if not.

### antithesis
This function would take a statement (thesis) and generate an opposing statement (antithesis). This involves understanding the core meaning of the thesis and forming its logical opposite, which can require reasoning and nuanced understanding, making it better suited for human/NLP tools. For example, antithesis('All cats are cute.') could generate 'Some cats are not cute'.

### synthesis
This function takes two statements (a thesis and its antithesis) and generates a new statement that attempts to reconcile the two, creating a synthesis of the ideas. This process involves understanding the relationship between the thesis and antithesis, then creating a higher level more refined idea. The function is better suited for human/NLP tools because the relationship between statements is complex and involves reasoning. For example, synthesis('All cats are cute.','Some cats are not cute') may return 'Most cats are cute, but not all'.

