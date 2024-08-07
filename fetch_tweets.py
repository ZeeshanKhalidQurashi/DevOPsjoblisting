import os
import requests
import json

API_KEY = os.getenv('SOCIAL_SEARCHER_API_KEY')
query = 'DevOps remote job'
url = f'https://api.social-searcher.com/v2/search?key={API_KEY}&q={query}&network=twitter'

response = requests.get(url)
data = response.json()

# Debugging: Print the entire response
print("API Response:")
print(json.dumps(data, indent=2))

# Extract relevant data
tweet_list = []
if 'posts' in data:
    for post in data['posts']:
        tweet_list.append({
            'text': post['text'],
            'created_at': post['published'],
            'user': post['user']['name']
        })

    # Save to a JSON file
    with open('tweets.json', 'w') as f:
        json.dump(tweet_list, f)
else:
    print("No 'posts' key in the response")

# Save the raw response for debugging purposes
with open('api_response.json', 'w') as f:
    json.dump(data, f)
