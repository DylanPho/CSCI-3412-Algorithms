'''
Name: Dylan Phoutthavong
Date: May 8th, 2025
Course: CSCI 3412
Task(s): Problem 1: Word Cloud and OBST
'''

import requests
import pprint
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# Step 1: Replace with your actual API key
API_KEY = '31a96b184b2042da9fbd4c037fa7f494'
QUERY = 'Denver'
PAGE_SIZE = 50  # Can be 20-100 for better results

# Step 2: Define endpoint and parameters
url = 'https://newsapi.org/v2/everything?'
parameters = {
    'q': QUERY,
    'pageSize': PAGE_SIZE,
    'language': 'en',
    'apiKey': API_KEY
}

# Step 3: Make the request and parse JSON
response = requests.get(url, params=parameters)
response_json = response.json()

# Step 4: Combine all headlines into one string
text_combined = ''
for article in response_json['articles']:
    text_combined += article['title'] + ' '

# Step 5: Generate the word cloud
wordcloud = WordCloud(max_font_size=40, background_color="white").generate(text_combined)

# Step 6: Display word cloud
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title(f"NewsAPI Word Cloud for '{QUERY}'")
plt.show()

# Step 7: Create frequency dict (needed for OBST)
def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)  # keep letters and spaces only
    return text.lower().split()

words = clean_text(text_combined)
counts = Counter(words)
total = sum(counts.values())
prob_dict = {word: freq / total for word, freq in counts.most_common(50)}

# Display top words and their probabilities
print("\nTop 50 Words with Probabilities:")
for word, prob in prob_dict.items():
    print(f"{word}: {prob:.4f}")
