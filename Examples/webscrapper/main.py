import os
from src.common import genai, content, json

# Import implemented functions
from src.scrape_web_for_news import scrape_web_for_news
from src.summarize import summarize

# Original implementation
def search(topic):
    text =scrape_web_for_news(topic) #use selenium and other web_scrapping tools non api 
    return summarize(text) #api tool that summarizes the text
print(search("Sam Altman"))