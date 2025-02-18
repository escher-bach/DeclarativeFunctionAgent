# webscrapper

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

### scrape_web_for_news
This function takes a search topic as input and scrapes the web for relevant news articles and text, then returns the raw text. It uses tools like Selenium and other web scraping libraries to gather information and does not need GenAI API.

### summarize
This function takes a large amount of text as input and returns a summarized version of the text, highlighting the key information using GenAI API.

