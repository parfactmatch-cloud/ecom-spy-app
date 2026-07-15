import json
import os

def process_and_build_database():
    print("🚀 Initiating EcomSpy Database Processing Stream...")
    
    # Path configuration
    raw_file = 'raw_data.json'
    output_file = 'data.json'
    
    if not os.path.exists(raw_file):
        print(f"❌ Error: {raw_file} not found! Creating a fallback template database.")
        fallback_data = [
            {
                "title": "💎 Diamond Crystal Rose LED Table Lamp",
                "platform": "TikTok Creative Center",
                "engagement": "3.2M Views | 140K Likes",
                "tag": "🔥 Live Trending Now",
                "roas": "3.5"
            }
        ]
        with open(raw_file, 'w', encoding='utf-8') as f:
            json.dump(fallback_data, f, indent=4, ensure_ascii=False)

    # Read Raw Input Database
    with open(raw_file, 'r', encoding='utf-8') as f:
        try:
            raw_products = json.load(f)
        except Exception as e:
            print(f"❌ JSON Parsing Error in raw_data.json: {e}")
            return

    processed_database = []

    for idx, item in enumerate(raw_products):
        title = item.get("title", "").strip()
        platform = item.get("platform", "").strip()
        engagement = item.get("engagement", "").strip()
        tag = item.get("tag", "").strip()
        roas_raw = str(item.get("roas", "2.5")).strip()

        if not title:
            continue

        # Format and sanitize parameters safely
        roas_clean = roas_raw.replace("x ROAS", "").replace("ROAS", "").strip()
        
        # Build optimized production output scheme
        processed_item = {
            "title": title,
            "platform": platform,
            "engagement": engagement,
            "tag": tag,
            "roas": f"{roas_clean}x ROAS" if "x" not in roas_clean else roas_clean
        }
        processed_database.append(processed_item)

    # Write highly-optimized WebApp delivery file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_database, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Data processing complete! {len(processed_database)} active products synced to {output_file}.")

if __name__ == "__main__":
    process_and_build_database()
  
