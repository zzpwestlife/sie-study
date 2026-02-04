
import re
from typing import List, Optional
from dataclasses import dataclass
import docx

@dataclass
class Block:
    content_en: str
    content_zh: Optional[str] = None
    type: str = "paragraph" # paragraph, heading, list_item, table, image
    level: int = 0 # For headings
    style: str = ""
    image_path: str = ""

class DocxParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = docx.Document(file_path)

    def parse(self) -> List[Block]:
        blocks = []
        # Identify blocks from docx
        for para in self.doc.paragraphs:
            text = para.text.strip()
            # Handle images (simplistic check for now, real extraction needs relations)
            # In python-docx, images are in runs.
            # We will come back to image extraction. 
            
            if not text:
                continue
            
            style_name = para.style.name
            
            # Basic classification
            if 'Heading' in style_name:
                try:
                    level = int(style_name.split(' ')[-1])
                except:
                    level = 1
                blocks.append(Block(content_en=text, type='heading', level=level, style=style_name))
            elif 'List' in style_name or text.startswith('»'):
                # Clean up list markers if necessary
                clean_text = text.lstrip('»').strip()
                blocks.append(Block(content_en=clean_text, type='list_item', style=style_name))
            else:
                # Default to paragraph
                # Heuristic: Check if it looks like a heading based on font size/bold? 
                # For now rely on style name and manual heuristics
                if len(text) < 100 and not text.strip().endswith(('.', ':', '!', '?')):
                     # Potential unstyled heading
                     blocks.append(Block(content_en=text, type='heading', style=style_name))
                else:
                    blocks.append(Block(content_en=text, type='paragraph', style=style_name))
                
        # Post-processing: Merge fragmented paragraphs
        merged_blocks = []
        if not blocks:
            return blocks
            
        current_block = blocks[0]
        
        for next_block in blocks[1:]:
            # Check if we should merge next_block into current_block
            should_merge = False
            
            if current_block.type == 'paragraph' and next_block.type == 'paragraph':
                # Heuristic 1: Current block ends with lowercase or comma, next starts with lowercase
                # D2 "these" -> D3 "types"
                curr_text = current_block.content_en.strip()
                next_text = next_block.content_en.strip()
                
                if not curr_text or not next_text:
                    should_merge = False
                else:
                    # Check end of current
                    ends_with_punct = curr_text[-1] in '.!?:;"'
                    starts_with_lower = next_text[0].islower()
                    
                    if not ends_with_punct:
                        # If it doesn't end with punctuation, it's a strong candidate for merging
                        # But be careful of headers that were misclassified as paragraphs
                        # (though we improved header detection above)
                        should_merge = True
                    elif ends_with_punct and starts_with_lower:
                        # Ends with punctuation but next starts lower? (e.g. "e.g. something")
                        should_merge = True
            
            if should_merge:
                # Merge
                current_block.content_en += " " + next_block.content_en
            else:
                merged_blocks.append(current_block)
                current_block = next_block
                
        merged_blocks.append(current_block)
        
        return merged_blocks

class MarkdownParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self) -> List[Block]:
        blocks = []
        with open(self.file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Simple parser for the specific bilingual format
        # Assumes: En block, then Zh block.
        # But looking at the file, it is interlaced lines/paragraphs.
        
        current_en = []
        current_zh = []
        
        # This is tricky because one paragraph might span multiple lines in MD?
        # Let's assume blank lines separate blocks.
        
        buffer = []
        for line in lines:
            line = line.strip()
            if not line:
                if buffer:
                    self._process_buffer(buffer, blocks)
                    buffer = []
            else:
                buffer.append(line)
        
        if buffer:
            self._process_buffer(buffer, blocks)
            
        return blocks

    def _split_mixed_line(self, line):
        # Heuristic: Find first Chinese character
        first_zh = -1
        for i, char in enumerate(line):
            if '\u4e00' <= char <= '\u9fff':
                first_zh = i
                break
        
        if first_zh == -1:
            return line, None
            
        # Backtrack to find separator
        split_idx = first_zh
        if split_idx > 0:
            # Check for opening parenthesis
            if line[split_idx-1] in ['(', '（']:
                split_idx -= 1
        
        en_text = line[:split_idx].strip()
        zh_text = line[split_idx:].strip()
        
        # Check if en_text has actual English words (at least one letter)
        # If not, treat as Chinese-only line (e.g. list markers "1. " or bold "**" followed by Chinese)
        if not any(c.isalpha() for c in en_text):
            return None, line
        
        return en_text, zh_text

    def _process_buffer(self, buffer, blocks):
        # Robust processing of buffer which might contain multiple blocks (e.g. list items)
        # that were grouped together because of no blank lines.
        
        i = 0
        while i < len(buffer):
            line = buffer[i]
            en, zh = self._split_mixed_line(line)
            
            # Check if this line is self-contained bilingual (has both substantial En and Zh)
            if zh and en:
                # It's a mixed line. Create a block.
                type_ = 'paragraph'
                level = 0
                
                if line.startswith('#'):
                    type_ = 'heading'
                    level = line.count('#')
                    # Remove hashes from content_en
                    en = en.lstrip('#').strip()
                elif re.match(r'^(\d+\.|[\*\-\•])\s+', line):
                    type_ = 'list_item'
                
                blocks.append(Block(content_en=en, content_zh=zh, type=type_, level=level))
                i += 1
                continue
            
            # If we are here, it's either En-only (zh is None) or Zh-only (en is None)
            # If Zh-only, it's an orphan Chinese line (unless we look back, but we iterate forward)
            # Actually, if it's Zh-only, we might have skipped it in the logic below?
            
            if zh and not en:
                 # Orphaned Chinese line (or maybe a header that was just Chinese?)
                 blocks.append(Block(content_en="", content_zh=zh))
                 i += 1
                 continue

            # It is En-only (en is line, zh is None). Look ahead.
            if i + 1 < len(buffer):
                next_line = buffer[i+1]
                next_en, next_zh = self._split_mixed_line(next_line)
                
                if next_zh and next_en:
                    # Next line is mixed.
                    # Heuristic: Is next_en just a few words (e.g. "SIE 考试") that might be part of the Chinese sentence?
                    # And it is NOT a list item or header?
                    is_header_or_list = next_line.startswith('#') or re.match(r'^(\d+\.|[\*\-\•])\s+', next_line)
                    is_short_en = len(next_en.split()) <= 3
                    
                    if not is_header_or_list and is_short_en:
                        # Treat next line as the translation for current line
                        # (Include the 'English' prefix in the Chinese content as it's likely part of the sentence)
                        blocks.append(Block(content_en=line, content_zh=next_line))
                        i += 2
                    else:
                        # It's a true separate mixed block (e.g. next item)
                        blocks.append(Block(content_en=line))
                        i += 1
                elif next_zh and not next_en:
                     # Next line is Chinese Only. Pair it!
                     blocks.append(Block(content_en=line, content_zh=next_zh))
                     i += 2
                else:
                     # Next line is En Only.
                     # Are they a pair? (En -> En?) No, usually En -> Zh.
                     # But check if next line LOOKS like Chinese?
                     # _split_mixed_line returns zh=None if no Chinese chars.
                     # So next line has no Chinese chars.
                     # It is En -> En.
                     blocks.append(Block(content_en=line))
                     i += 1
            else:
                # Last line, En-only
                blocks.append(Block(content_en=line))
                i += 1

    def _is_english(self, text):
        # Simple heuristic: count ASCII vs non-ASCII
        ascii_count = sum(1 for c in text if ord(c) < 128)
        return ascii_count > len(text) * 0.5

if __name__ == "__main__":
    # Test
    dp = DocxParser("Chapters_translate/Chapter_5.docx")
    docx_blocks = dp.parse()
    print(f"Docx blocks: {len(docx_blocks)}")
    
    mp = MarkdownParser("Chapters_translate/chapter5_bilingual.md")
    md_blocks = mp.parse()
    print(f"MD blocks: {len(md_blocks)}")
    
    # Print sample
    for b in md_blocks[:5]:
        zh_preview = b.content_zh[:20] if b.content_zh else "None"
        print(f"MD: {b.content_en[:20]}... | {zh_preview}...")
