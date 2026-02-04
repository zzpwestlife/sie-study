
import sys
import os
sys.path.append(os.getcwd())
from pipeline.parser import DocxParser, MarkdownParser

def debug():
    dp = DocxParser("Chapters_translate/Chapter_6.docx")
    docx_blocks = dp.parse()
    print(f"Docx Blocks: {len(docx_blocks)}")
    for i, b in enumerate(docx_blocks[:10]):
        print(f"D{i}: [{b.type}] {b.content_en}")

    mp = MarkdownParser("Chapters_translate/chapter6_bilingual.md")
    md_blocks = mp.parse()
    print(f"MD Blocks: {len(md_blocks)}")
    for i, b in enumerate(md_blocks[:15]):
        zh = b.content_zh if b.content_zh else ""
        print(f"M{i}: [{b.type}] En: {b.content_en[:50]}... | Zh: {zh[:50]}...")

if __name__ == "__main__":
    debug()
