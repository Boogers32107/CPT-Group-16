import requests
import random

headline_list = [] # Need list of headlines or something Problably from X/Twitter

def generate_haiku():
    syllables = [5, 7, 5]
    haiku = []
    for s in syllables:
        line = ' '.join(random.choice(headline_list) for _ in range(s)) 
    return '\n'.join(haiku)

def post_to_discord(haiku):
    webhook_url = "Teacher will provide webhook"
    payload = { "content": haiku }
    response = requests.post(webhook_url, json=payload)
    print(response.status_code)

if __name__ == "__main__":
    haiku = generate_haiku()
    post_to_discord(haiku)