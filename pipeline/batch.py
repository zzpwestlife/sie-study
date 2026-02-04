
import os
import re
import glob
import json
from pipeline.parser import DocxParser, MarkdownParser
from pipeline.merger import ContentMerger

OUTPUT_DIR = "output"
ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")

def ensure_dirs():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)

def get_chapter_number(filename):
    match = re.search(r'Chapter_(\d+)', filename)
    if match:
        return int(match.group(1))
    return 0

import shutil

def process_all(src_dir):
    ensure_dirs()
    
    docx_files = glob.glob(os.path.join(src_dir, "Chapter_*.docx"))
    results = []
    
    for docx_path in sorted(docx_files, key=lambda x: get_chapter_number(os.path.basename(x))):
        filename = os.path.basename(docx_path)
        chapter_num = get_chapter_number(filename)
        
        # Copy PDF if exists
        pdf_filename = f"Chapter_{chapter_num}.pdf"
        pdf_src = os.path.join(src_dir, pdf_filename)
        if os.path.exists(pdf_src):
            shutil.copy2(pdf_src, os.path.join(OUTPUT_DIR, pdf_filename))
        else:
            pdf_filename = ""

        # Find corresponding MD file
        # Expected: chapter{N}_bilingual.md
        md_filename = f"chapter{chapter_num}_bilingual.md"
        md_path = os.path.join(src_dir, md_filename)
        
        if not os.path.exists(md_path):
            print(f"Warning: Markdown file not found for {filename}: {md_path}")
            continue
            
        print(f"Processing Chapter {chapter_num}...")
        
        dp = DocxParser(docx_path)
        mp = MarkdownParser(md_path)
        
        merger = ContentMerger(dp.parse(), mp.parse())
        merger.merge()
        
        # Generate HTML
        html_content = merger.generate_html(f"Chapter {chapter_num}", pdf_filename)
        html_filename = f"chapter{chapter_num}.html"
        html_path = os.path.join(OUTPUT_DIR, html_filename)
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        stats = merger.stats
        stats['chapter'] = chapter_num
        stats['html_file'] = html_filename
        results.append(stats)
        
    return results

def generate_index(results):
    html = ["""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SIE Study Guide - Translations</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .progress-bar { background-color: #eee; height: 20px; width: 100px; }
        .progress-fill { background-color: #4caf50; height: 100%; }
    </style>
</head>
<body>
    <h1>SIE Study Guide - Bilingual Chapters</h1>
    <table>
        <thead>
            <tr>
                <th>Chapter</th>
                <th>Blocks</th>
                <th>Matched</th>
                <th>Missing Trans</th>
                <th>Coverage</th>
            </tr>
        </thead>
        <tbody>"""]
        
    for res in results:
        total = res['total_docx_blocks']
        matched = res['matched_blocks']
        missing = res['missing_translation']
        coverage = (matched / total * 100) if total > 0 else 0
        
        html.append(f"""
            <tr>
                <td><a href="{res['html_file']}">Chapter {res['chapter']}</a></td>
                <td>{total}</td>
                <td>{matched}</td>
                <td>{missing}</td>
                <td>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {coverage}%"></div>
                    </div>
                    {coverage:.1f}%
                </td>
            </tr>""")
            
    html.append("""
        </tbody>
    </table>
</body>
</html>""")
    
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write("\n".join(html))

if __name__ == "__main__":
    src_dir = "Chapters_translate"
    results = process_all(src_dir)
    generate_index(results)
    print("Batch processing complete.")
