
import difflib
import os
import sys
import re
# Add current directory to path so we can run this script directly if needed
sys.path.append(os.getcwd())

from pipeline.parser import Block, DocxParser, MarkdownParser

class ContentMerger:
    def __init__(self, docx_blocks: List[Block], md_blocks: List[Block]):
        self.docx_blocks = docx_blocks
        self.md_blocks = md_blocks
        self.merged_blocks = []
        self.stats = {
            "total_docx_blocks": len(docx_blocks),
            "matched_blocks": 0,
            "missing_translation": 0
        }

    def merge(self) -> List[Block]:
        # Simple greedy matching
        # For each docx block, scan md_blocks for a match
        
        md_idx = 0
        max_md_idx = len(self.md_blocks)
        
        # Debug log
        debug_f = open("merge_debug.log", "w", encoding="utf-8")
        
        for docx_block in self.docx_blocks:
            best_match = None
            best_ratio = 0.0
            best_idx = -1
            
            # Search window: current md_idx to md_idx + 50
            # Also look BACK a bit (e.g. 5 blocks) in case of slight reordering or misalignment
            search_start = max(0, md_idx - 5)
            search_end = min(md_idx + 50, max_md_idx)
            
            for i in range(search_start, search_end):
                md_b = self.md_blocks[i]
                
                # Normalize for comparison
                d_text = self._normalize(docx_block.content_en)
                m_text = self._normalize(md_b.content_en)
                
                if not d_text: continue
                
                ratio = difflib.SequenceMatcher(None, d_text, m_text).ratio()
                
                if ratio > 0.6: # Lower threshold to 0.6
                    if ratio > best_ratio:
                        best_ratio = ratio
                        best_match = md_b
                        best_idx = i
            
            if best_match:
                # Found a match
                docx_block.content_zh = best_match.content_zh
                
                debug_f.write(f"[MATCH {best_ratio:.2f}] Docx: {docx_block.content_en[:30]}... <--> MD: {best_match.content_en[:30]}...\n")
                
                # If the match was a "Same Line" bilingual heading (e.g. "# En Zh")
                if not docx_block.content_zh and best_match.content_en:
                     if any(ord(c) > 128 for c in best_match.content_en):
                         if best_match.content_en.startswith(docx_block.content_en):
                             remainder = best_match.content_en[len(docx_block.content_en):].strip()
                             docx_block.content_zh = remainder
                
                self.stats["matched_blocks"] += 1
                if not docx_block.content_zh:
                    self.stats["missing_translation"] += 1
                    debug_f.write(f"  -> Match found but no Chinese content extracted.\n")
                
                # Advance md_idx to best_idx + 1 to keep order
                # But don't jump too far if we skipped some?
                # Trust the best match implies we moved forward.
                md_idx = best_idx + 1
            else:
                self.stats["missing_translation"] += 1
                debug_f.write(f"[MISSING] Docx: {docx_block.content_en[:50]}...\n")
                # Try to see what was in the search window
                # debug_f.write(f"  Window start: {self.md_blocks[search_start].content_en[:20]}...\n")
            
            self.merged_blocks.append(docx_block)
            
        debug_f.close()
        return self.merged_blocks

    def _normalize(self, text):
        # Remove common list markers and lowercase
        text = text.lower().strip()
        # Replace smart quotes
        text = text.replace('’', "'").replace('“', '"').replace('”', '"')
        
        # Remove leading numbers (1., 1.1, etc)
        # Regex: Start of string, digits/dots, space
        text = re.sub(r'^\s*[\d\.]+\s+', '', text)
        
        # Remove markdown list markers
        text = text.lstrip('*').lstrip('-').lstrip('•').strip()
        # Remove docx list markers (like '»')
        text = text.lstrip('»').strip()
        return text

    def generate_html(self, chapter_title: str, pdf_filename: str = "") -> str:
        # Generate HTML from merged blocks
        html = []
        html.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter_title}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" rel="stylesheet" />
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; max-width: 1200px; margin: 0 auto; padding: 20px; display: flex; background-color: #f9f9f9; }}
        .sidebar {{ width: 280px; position: sticky; top: 20px; height: 95vh; overflow-y: auto; padding-right: 20px; border-right: 1px solid #ddd; font-size: 0.9em; }}
        .sidebar ul {{ list-style: none; padding-left: 0; }}
        .sidebar li {{ margin-bottom: 8px; }}
        .sidebar a {{ text-decoration: none; color: #0066cc; }}
        .sidebar a:hover {{ text-decoration: underline; }}
        
        .content {{ flex: 1; padding-left: 50px; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }}
        
        .header-actions {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; border-bottom: 1px solid #eee; padding-bottom: 20px; }}
        .btn {{ display: inline-block; padding: 8px 16px; background-color: #0066cc; color: white; text-decoration: none; border-radius: 4px; font-weight: 500; transition: background 0.2s; }}
        .btn:hover {{ background-color: #004d99; }}
        
        .block {{ margin-bottom: 2em; }}
        .block-en {{ color: #222; font-size: 1.1em; }}
        .block-zh {{ color: #555; margin-top: 0.8em; padding-left: 1em; border-left: 3px solid #eee; }}
        
        h1, h2, h3, h4 {{ color: #1a1a1a; margin-top: 1.5em; }}
        h1 {{ font-size: 2.2em; border-bottom: 2px solid #0066cc; padding-bottom: 10px; }}
        h2 {{ font-size: 1.8em; }}
        
        .missing-trans {{ background-color: #fff8e1; color: #b00; border-left-color: #ffc107; font-style: italic; }}
        
        /* Accessibility */
        :focus {{ outline: 3px solid #0066cc; outline-offset: 2px; }}
    </style>
</head>
<body>
    <nav class="sidebar" aria-label="Table of Contents">
        <h3>Contents</h3>
        <ul>
            <li><a href="../index.html">← Back to Index</a></li>
            <hr>""")
        
        # TOC
        for b in self.merged_blocks:
            if b.type == 'heading':
                indent = (b.level - 1) * 15
                html.append(f'<li style="padding-left: {indent}px"><a href="#block-{id(b)}">{b.content_en[:40]}...</a></li>')
        
        html.append(f"""</ul>
    </nav>
    <main class="content">
        <div class="header-actions">
            <h1>{chapter_title}</h1>
            {f'<a href="{pdf_filename}" class="btn" download>Download PDF</a>' if pdf_filename else ''}
        </div>""")
        
        # Content
        for b in self.merged_blocks:
            block_id = f"block-{id(b)}"
            
            # Heading
            if b.type == 'heading':
                tag = f"h{b.level}"
                html.append(f'<section class="block heading" id="{block_id}">')
                html.append(f'<{tag}>{b.content_en}</{tag}>')
                if b.content_zh:
                    html.append(f'<div class="block-zh">{b.content_zh}</div>')
                html.append('</section>')
            
            # List Item
            elif b.type == 'list_item':
                html.append(f'<div class="block list-item" id="{block_id}">')
                html.append(f'<div class="block-en">• {b.content_en}</div>')
                if b.content_zh:
                    html.append(f'<div class="block-zh">{b.content_zh}</div>')
                else:
                    html.append('<div class="block-zh missing-trans">[Missing Translation]</div>')
                html.append('</div>')
            
            # Paragraph
            else:
                html.append(f'<section class="block paragraph" id="{block_id}">')
                html.append(f'<p class="block-en">{b.content_en}</p>')
                if b.content_zh:
                    html.append(f'<p class="block-zh">{b.content_zh}</p>')
                else:
                    html.append('<p class="block-zh missing-trans">[Missing Translation]</p>')
                html.append('</section>')
                
        html.append("""
    </main>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js"></script>
</body>
</html>""")
        
        return "\n".join(html)

if __name__ == "__main__":
    # Test
    dp = DocxParser("Chapters_translate/Chapter_5.docx")
    mp = MarkdownParser("Chapters_translate/chapter5_bilingual.md")
    
    merger = ContentMerger(dp.parse(), mp.parse())
    merger.merge()
    print("Stats:", merger.stats)
    
    html = merger.generate_html("Chapter 5")
    with open("chapter5_test.html", "w", encoding="utf-8") as f:
        f.write(html)
