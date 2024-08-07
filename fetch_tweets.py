import requests
import json

API_KEY = 'your_social_searcher_api_key'
query = 'DevOps remote job'
url = f'https://api.social-searcher.com/v2/search?key={API_KEY}&q={query}&network=twitter'

response = requests.get(url)
data = response.json()

# Extract relevant data
tweet_list = []
for post in data['posts']:
    tweet_list.append({
        'text': post['text'],
        'created_at': post['published'],
        'user': post['user']['name']
    })

# Save to a JSON file
with open('tweets.json', 'w') as f:
    json.dump(tweet_list, f)
