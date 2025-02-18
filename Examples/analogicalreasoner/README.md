# analogicalreasoner

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

### find_correspondences
This function will identify similarities and relationships between the 'source' and 'target' input strings, leveraging an API to find commonalities. For example, it might find that 'a bird' in the source corresponds to 'an airplane' in the target based on the shared concept of 'flying'. Requires genai API

### transfer_knowledge
This function will take the 'source' input string and a mapping derived from the find_correspondences function, and transfer relevant knowledge from the source to the target based on this mapping. This requires natural language understanding and reasoning, making it better suited for human/NLP tools. For example, if the source describes how a bird uses its wings to fly, and the mapping connects 'bird' to 'airplane', this function might generate text explaining how an airplane uses its wings for flight, which requires GenAI.

