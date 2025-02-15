import requests
from bs4 import BeautifulSoup
import random

def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        headlines = soup.find_all(["h1", "h2", "h3"])
        headline_texts = [headline.get_text().strip() for headline in headlines]

        return headline_texts if headline_texts else ["No headlines found on this page."]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []


if __name__ == "__main__":
    url = "https://www.foxnews.com/story/"
    headline = scrape_headlines(url)
    if headline:
        print(headline)