def search(topic):
    text =scrape_web_for_news(topic) #use selenium and other web_scrapping tools non api 
    return summarize(text) #api tool that summarizes the text
