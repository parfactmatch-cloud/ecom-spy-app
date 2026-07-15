import json
import requests
from bs4 import BeautifulSoup
import os

def scrape_data():
    products = []
    # Hum yahan Pinterest Trends ki public search query URL ka example le rahe hain
    # Aap yahan apna target URL badal sakte hain
    target_url = "https://trends.pinterest.com/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # NOTE: Selector (h2.title) website ke hisab se badalna padega
        # Yeh ek example structure hai.
        items = soup.select('.trend-card') # Class name aapko inspect element karke check karna hoga
        
        for item in items[:5]: # Sirf top 5 uthate hain
            title = item.select_one('.title').text.strip() if item.select_one('.title') else "New Trending Item"
            products.append({
                "title": title,
                "platform": "Pinterest Trends",
                "engagement": "Real-time Live",
                "tag": "🔥 Auto-Scraped",
                "roas": "3.0x ROAS"
            })
    except Exception as e:
        print(f"Scraping failed, using fallback: {e}")
        
    return products

def process():
    # Scrap kiya hua data ya manual fallback
    new_data = scrape_data()
    
    if not new_data:
        # Fallback agar scraping fail ho jaye
        new_data = [{"title": "Trending Niche Product", "platform": "AI Feed", "engagement": "Live", "tag": "New", "roas": "2.5x ROAS"}]
        
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    process()
    
