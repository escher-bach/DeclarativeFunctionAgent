# greatyjoke

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

### generate_joke
This function takes a topic as input and returns a joke related to that topic. Because joke generation requires creativity and an understanding of humor, which is subjective and difficult to codify, it's better suited for human/NLP tools.  For example, generate_joke('cats') might return 'Why don't cats play poker in the wild? Too many cheetahs!'

