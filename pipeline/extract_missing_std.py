import re
import json
import sys

def extract_missing_entries(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []

    # Find all blocks that contain missing-trans
    # We look for the pattern: id="block-XYZ" ... class="block-en">ENGLISH_TEXT< ... class="block-zh missing-trans">
    # Since the order of attributes or tags might vary slightly, we can iterate through the file
    # or use a regex that captures the ID and the English text for each missing-trans occurrence.
    
    # Strategy:
    # 1. Split content into blocks (assuming blocks are div or section with id="block-...")
    # This is hard with regex split.
    
    # Alternative Strategy:
    # Find all 'missing-trans' indices.
    # For each index, search backwards for 'id="block-..."' and 'class="block-en">...<'
    
    missing_items = []
    
    # Find all occurrences of missing-trans
    missing_iter = re.finditer(r'class="block-zh missing-trans">', content)
    
    for match in missing_iter:
        start_index = match.start()
        
        # Search backwards for the block ID
        # We look for id="block-..." before the current position
        # We limit the search to, say, 1000 characters back to avoid false positives from far away blocks
        preceding_text = content[max(0, start_index - 1000):start_index]
        
        # Find the last ID in the preceding text
        id_matches = list(re.finditer(r'id="(block-[0-9]+)"', preceding_text))
        if not id_matches:
            print(f"Warning: Could not find ID for missing translation at index {start_index}")
            continue
            
        block_id = id_matches[-1].group(1)
        
        # Find the English text
        # It should be in class="block-en">...</div> or ...</p> inside the same block
        # We assume the block-en comes before block-zh
        
        # Find the last block-en in the preceding text
        en_matches = list(re.finditer(r'class="block-en">(.*?)(</div>|</p>)', preceding_text, re.DOTALL))
        
        if en_matches:
            en_text = en_matches[-1].group(1).strip()
            missing_items.append({
                'id': block_id,
                'en_text': en_text
            })
        else:
            print(f"Warning: Could not find English text for block {block_id}")

    return missing_items

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_missing_std.py <file_path>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    items = extract_missing_entries(file_path)
    print(json.dumps(items, indent=2, ensure_ascii=False))
