import requests
import random
from headlinescraper import scrape_headlines

def generate_haiku(headline_list):
    syllables = [5, 7, 5]
    haiku = []
    for s in syllables:
        line = ' '.join(random.choice(headline_list) for _ in range(s))
        haiku.append(line)
    return '\n'.join(haiku)

def post_to_discord(haiku):
    webhook_url = 'https://discord.com/api/webhooks/1339685758273061016/COYZDNyTFckb1PX2PDalu-LUnaea-BEIeQsG9c4ca1my9x2dZTmITiFinjRkjN0Dhini'
    payload = { "content": f"Generated Haiku Group 16:\n{haiku}" }
    response = requests.post(webhook_url, json=payload)
    print(response.status_code)
    print("Haiku posted to Discord:")
    print(haiku)

if __name__ == "__main__":
    url = "https://www.foxnews.com/story/foxnews-com-rss-feeds"
    headlines = scrape_headlines(url)
    if headlines:
        haiku = generate_haiku(headlines)
        post_to_discord(haiku)