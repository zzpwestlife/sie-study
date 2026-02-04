
import re
from bs4 import BeautifulSoup

def extract_missing(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    missing_blocks = soup.find_all(class_='missing-trans')
    
    results = []
    for missing in missing_blocks:
        parent = missing.parent
        # Find the English block
        en_block = parent.find(class_='block-en')
        if en_block:
            block_id = parent.get('id')
            text = en_block.get_text().strip()
            # Clean up list markers if present in text (though parser might have kept them)
            # The parser output shows "• " prefix for list items in block-en div
            results.append((block_id, text))
            
    return results

if __name__ == "__main__":
    items = extract_missing("output/chapter5.html")
    for bid, text in items:
        print(f"ID: {bid}")
        print(f"EN: {text}")
        print("-" * 20)
