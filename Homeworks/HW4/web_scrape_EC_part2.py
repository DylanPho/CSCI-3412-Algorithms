import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Set target URL
url = "https://quotes.toscrape.com"

# Step 2: Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract quote blocks
quote_blocks = soup.find_all("div", class_="quote")
quotes_data = []

for block in quote_blocks:
    text = block.find("span", class_="text").get_text(strip=True)
    author = block.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in block.find_all("a", class_="tag")]
    quotes_data.append({
        "quote": text,
        "author": author,
        "tags": ", ".join(tags)
    })

# Step 4: Save to CSV
with open("quotes.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    for row in quotes_data:
        writer.writerow(row)

print("✅ Quotes scraped and saved to 'quotes.csv'")
