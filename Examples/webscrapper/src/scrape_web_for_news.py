from newsapi import NewsApiClient
from datetime import datetime, timedelta

def scrape_web_for_news(search_topic):
    """This function fetches news articles about a given topic using NewsAPI.

    Args:
        search_topic (str): The topic to search for news articles about.

    Returns:
        str: A string containing the raw text of the news articles.
             Returns an empty string if an error occurs.
    """
    try:
        # Initialize NewsAPI client
        # Replace 'YOUR_API_KEY' with your actual NewsAPI key
        newsapi = NewsApiClient(api_key='60dbc954a760425d949bc917a81b40f6')
        
        # Calculate date range (last 7 days)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        # Fetch articles
        articles = newsapi.get_everything(
            q=search_topic,
            language='en',
            sort_by='relevancy',
            from_param=start_date.strftime('%Y-%m-%d'),
            to=end_date.strftime('%Y-%m-%d'),
            page_size=5  # Limit to 5 articles
        )
        
        # Process and format the results
        raw_text = ""
        
        if articles['status'] == 'ok':
            for article in articles['articles']:
                # Add article title
                raw_text += f"Title: {article['title']}\n"
                raw_text += f"Source: {article['source']['name']}\n"
                raw_text += f"Date: {article['publishedAt']}\n\n"
                
                # Add article description and content
                if article['description']:
                    raw_text += f"{article['description']}\n\n"
                if article['content']:
                    raw_text += f"{article['content']}\n"
                    
                raw_text += "-" * 80 + "\n\n"
                
        return raw_text.strip()

    except ImportError:
        print("Please install required package: pip install newsapi-python")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""
    
if __name__ == "__main__":
    result = scrape_web_for_news("artificial intelligence")
    print(result)


