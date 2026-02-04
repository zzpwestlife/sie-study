import re
import json
import sys

def apply_translations(html_file, map_file):
    try:
        with open(map_file, 'r', encoding='utf-8') as f:
            translations_list = json.load(f)
    except FileNotFoundError:
        print(f"Error: Map file {map_file} not found.")
        return

    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: HTML file {html_file} not found.")
        return
        
    applied_count = 0
    failed_count = 0
    
    # Convert list to dict for easier lookup if needed, but we iterate
    for item in translations_list:
        block_id = item['id']
        translation = item['translation']
        
        # Determine the tag type for the block-zh element based on observation
        # Usually paragraph -> p, list-item -> div
        # But we can capture the tag name in regex
        
        # Regex explanation:
        # 1. Match the opening tag of the container (section or div) with the specific ID.
        #    (<(section|div)[^>]*id="BLOCK_ID"[^>]*>)
        # 2. Match everything until the missing-trans element.
        #    (.*?)
        # 3. Match the missing-trans element. Capture the tag name (p or div).
        #    (<(p|div) class="block-zh missing-trans">.*?<\/\4>)
        #    Note: \4 refers to the 4th group which is (p|div). 
        #    Actually, let's simplify group numbering.
        
        # Simplified Regex:
        # Group 1: Container start tag with ID
        # Group 2: Content before block-zh
        # Group 3: block-zh start tag including class
        # Group 4: Inner content of block-zh (to be replaced)
        # Group 5: block-zh end tag
        # Group 6: Remaining content until container end
        
        # Since we want to replace the whole block-zh element to remove "missing-trans" class,
        # we can just match the whole element.
        
        # Pattern:
        # (<(?:section|div)[^>]*id="re.escape(block_id)"[^>]*>.*?)(<(p|div) class="block-zh missing-trans">)(.*?)(<\/\3>)(.*?</(?:section|div)>)
        
        # Wait, the closing tag of the container needs to match the opening tag.
        # But since we are doing one replacement per ID, we can be a bit looser or just use non-greedy matching.
        
        # Let's try to match the container start, then find the block-zh missing-trans inside it.
        # Since we load the whole file, we need to be careful not to match across blocks.
        # But the blocks are closed.
        
        pattern = r'(<(section|div)[^>]*id="' + re.escape(block_id) + r'"[^>]*>.*?)(<(p|div) class="block-zh missing-trans">)(.*?)(<\/\4>)'
        
        # Replacement:
        # \1 (container start + English part)
        # <\3 class="block-zh"> (start tag with class modified)
        # translation
        # \6 (end tag)
        
        # Note: \3 is the tag name (p or div)
        
        def replace_callback(match):
            # match.group(1): Container start ... until block-zh start
            # match.group(2): section or div (container tag)
            # match.group(3): block-zh start tag
            # match.group(4): p or div (inner tag)
            # match.group(5): content inside block-zh
            # match.group(6): block-zh end tag
            
            part1 = match.group(1)
            tag_name = match.group(4)
            
            return f'{part1}<{tag_name} class="block-zh">{translation}</{tag_name}>'
            
        new_content, count = re.subn(pattern, replace_callback, content, flags=re.DOTALL)
        
        if count > 0:
            content = new_content
            applied_count += 1
            # print(f"Applied: {block_id}")
        else:
            print(f"Failed to match: {block_id}")
            failed_count += 1

    print(f"Total applied: {applied_count}")
    print(f"Total failed: {failed_count}")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    html_file = 'output/chapter5.html'
    map_file = 'pipeline/translations_map.json'
    apply_translations(html_file, map_file)
