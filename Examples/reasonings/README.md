# reasonings

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

### find_patterns
This function analyzes a set of observations (input string) to identify recurring patterns or relationships within the data. It returns a string representing the identified patterns.

### generalize
This function takes the identified patterns as input and forms a general hypothesis or rule that explains those patterns. It is more complex because it takes an arbitary string as input and forms a logical guess.

### explains
This function evaluates whether a given hypothesis adequately explains a set of observations. It would return true if the hypothesis explains observations and false if it doesn't. For example, the hypothesis 'All birds can fly' explains the observation 'Sparrows can fly' but may not explain the observation 'penguins cannot fly'

### is_most_plausible
This function assesses the plausibility or likelihood of a given hypothesis compared to other possible explanations. In a set of potential statements it picks the best one.

