
import docx
import sys
import os

def analyze_docx(file_path):
    doc = docx.Document(file_path)
    print(f"Analyzing {file_path}...")
    
    for i, para in enumerate(doc.paragraphs):
        if not para.text.strip():
            continue
        print(f"Para {i}: Style='{para.style.name}', Text='{para.text[:50]}...'")
        if i > 100: break

if __name__ == "__main__":
    file_path = "Chapters_translate/Chapter_5.docx"
    if os.path.exists(file_path):
        analyze_docx(file_path)
    else:
        print(f"File not found: {file_path}")
