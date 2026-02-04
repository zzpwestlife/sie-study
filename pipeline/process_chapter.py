import sys
import os
import re
# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline.parser import DocxParser, MarkdownParser
from pipeline.merger import ContentMerger

OUTPUT_DIR = "output"
SRC_DIR = "Chapters_translate"

def process_chapter(chapter_num):
    docx_filename = f"Chapter_{chapter_num}.docx"
    docx_path = os.path.join(SRC_DIR, docx_filename)
    
    md_filename = f"chapter{chapter_num}_bilingual.md"
    md_path = os.path.join(SRC_DIR, md_filename)
    
    if not os.path.exists(docx_path):
        print(f"Error: Docx file not found: {docx_path}")
        return
        
    if not os.path.exists(md_path):
        print(f"Error: Markdown file not found: {md_path}")
        return

    print(f"Processing Chapter {chapter_num}...")
    
    dp = DocxParser(docx_path)
    mp = MarkdownParser(md_path)
    
    merger = ContentMerger(dp.parse(), mp.parse())
    merger.merge()
    
    # Generate HTML
    pdf_filename = f"Chapter_{chapter_num}.pdf"
    pdf_src = os.path.join(SRC_DIR, pdf_filename)
    if not os.path.exists(pdf_src):
        pdf_filename = ""
    else:
        # Copy PDF to output if not there
        import shutil
        dst_pdf = os.path.join(OUTPUT_DIR, pdf_filename)
        if not os.path.exists(dst_pdf):
             shutil.copy2(pdf_src, dst_pdf)
        
    html_content = merger.generate_html(f"Chapter {chapter_num}", pdf_filename)
    html_filename = f"chapter{chapter_num}.html"
    html_path = os.path.join(OUTPUT_DIR, html_filename)
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Generated {html_path}")
    print(f"Stats: {merger.stats}")
    
    # Check for missing translations
    if merger.stats['missing_translation'] > 0:
        print(f"WARNING: {merger.stats['missing_translation']} blocks missing translations!")
        
        print("\n--- First 20 Missing Blocks ---")
        count = 0
        for i, block in enumerate(merger.merged_blocks):
            if not block.content_zh:
                print(f"Missing [{i}]: {block.content_en[:100]}...")
                count += 1
                if count >= 20:
                    break
        print("-------------------------------\n")
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_chapter.py <chapter_number>")
        sys.exit(1)
    
    process_chapter(sys.argv[1])
