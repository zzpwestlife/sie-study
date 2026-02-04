
import unittest
from pipeline.parser import Block, MarkdownParser, DocxParser
from pipeline.merger import ContentMerger

class TestMarkdownParser(unittest.TestCase):
    def test_split_bilingual_header(self):
        # Create a mock file or just test the logic if I can extract it?
        # Since logic is inside _process_buffer, and it's called by parse() which reads file.
        # I'll create a temp file.
        with open("test_md.md", "w", encoding="utf-8") as f:
            f.write("# Chapter 5: Title 标题\n\n")
            f.write("Some English text.\nSome Chinese text.\n")
        
        mp = MarkdownParser("test_md.md")
        blocks = mp.parse()
        
        # Check Header
        self.assertEqual(blocks[0].type, 'heading')
        self.assertEqual(blocks[0].content_en, "Chapter 5: Title")
        self.assertEqual(blocks[0].content_zh, "标题")
        
        # Check Paragraph
        self.assertEqual(blocks[1].content_en, "Some English text.")
        self.assertEqual(blocks[1].content_zh, "Some Chinese text.")
        
        import os
        os.remove("test_md.md")

class TestMerger(unittest.TestCase):
    def test_merge_exact_match(self):
        docx_blocks = [Block(content_en="Hello World")]
        md_blocks = [Block(content_en="Hello World", content_zh="你好世界")]
        
        merger = ContentMerger(docx_blocks, md_blocks)
        merged = merger.merge()
        
        self.assertEqual(merged[0].content_zh, "你好世界")
        self.assertEqual(merger.stats['matched_blocks'], 1)

    def test_merge_fuzzy_match(self):
        docx_blocks = [Block(content_en="Hello World!")]
        md_blocks = [Block(content_en="hello world", content_zh="你好世界")]
        
        merger = ContentMerger(docx_blocks, md_blocks)
        merged = merger.merge()
        
        self.assertEqual(merged[0].content_zh, "你好世界")

if __name__ == '__main__':
    unittest.main()
