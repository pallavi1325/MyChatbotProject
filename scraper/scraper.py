import requests
from bs4 import BeautifulSoup
import json

# Define headers to simulate a request from a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Function to scrape the content
def scrape_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract headings and content
    headings = soup.find_all(['h1', 'h2', 'h3'])
    content = soup.find_all('p')

    data = []
    seen_content = set()  # A set to track seen content and avoid duplication

    for heading in headings:
        content_text = ''
        for paragraph in content:
            text = paragraph.get_text(strip=True)

            # Skip unwanted content (like footers or promotional sections)
            if any(keyword in text for keyword in ['Product', 'For Developers', 'Support']):
                continue

            # Check if the content is repeated
            if text in seen_content:
                continue  # Skip if content is already seen

            # Clean and append content
            if text:
                content_text += text + '\n'
                seen_content.add(text)  # Mark this content as seen
        
        # Clean up heading text
        heading_text = heading.get_text(strip=True)
        
        # Only add data if there's meaningful content
        if heading_text and content_text.strip():
            data.append({'heading': heading_text, 'content': content_text.strip()})

    return data

# List of URLs to scrape
urls = {
    "Segment": "https://segment.com/docs/?ref=nav",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

# Scrape each URL and save the result
scraped_data = {}
for platform, url in urls.items():
    print(f"Starting to scrape {platform} documentation...")
    scraped_data[platform] = scrape_page(url)

# Save the scraped data into a JSON file
with open('scraped_data.json', 'w') as json_file:
    json.dump(scraped_data, json_file, indent=4)

print("Scraping completed.")
