
import re

def assemble_ch15_16():
    # Process Ch 15
    with open('SIE Exam 20252026 For Dummies/temp_ch15_english.md', 'r', encoding='utf-8') as f:
        ch15_raw = f.read()
        
    split_marker = "Testing Your Knowledge"
    idx_split = ch15_raw.find(split_marker)
    if idx_split != -1:
        ch15_body_english = ch15_raw[:idx_split]
    else:
        # Try "Practice questions"
        idx_split = ch15_raw.find("Practice questions")
        if idx_split != -1:
             ch15_body_english = ch15_raw[:idx_split]
        else:
             ch15_body_english = ch15_raw
        
    with open('SIE Exam 20252026 For Dummies/chapter15_bilingual.md', 'r', encoding='utf-8') as f:
        ch15_original = f.read()
        
    overlap = "Touring the tax categories"
    overlap_idx = ch15_body_english.find(overlap)
    
    if overlap_idx != -1:
        line_end = ch15_body_english.find('\n', overlap_idx)
        ch15_append = ch15_body_english[line_end+1:]
    else:
        if "Touring" in ch15_body_english:
             overlap_idx = ch15_body_english.find("Touring")
             line_end = ch15_body_english.find('\n', overlap_idx)
             ch15_append = ch15_body_english[line_end+1:]
        else:
             ch15_append = ch15_body_english
        
    with open('SIE Exam 20252026 For Dummies/ch15_questions_translated.md', 'r', encoding='utf-8') as f:
        ch15_questions = f.read()
        
    final_ch15 = ch15_original + "\n\n" + ch15_append + "\n\n" + ch15_questions
    
    with open('SIE Exam 20252026 For Dummies/chapter15_bilingual.md', 'w', encoding='utf-8') as f:
        f.write(final_ch15)
        
    # Process Ch 16
    with open('SIE Exam 20252026 For Dummies/temp_ch16_english.md', 'r', encoding='utf-8') as f:
        ch16_raw = f.read()
        
    idx_split = ch16_raw.find(split_marker)
    if idx_split != -1:
        ch16_body_english = ch16_raw[:idx_split]
    else:
         idx_split = ch16_raw.find("Practice questions")
         if idx_split != -1:
             ch16_body_english = ch16_raw[:idx_split]
         else:
             ch16_body_english = ch16_raw
        
    with open('SIE Exam 20252026 For Dummies/chapter16_bilingual.md', 'r', encoding='utf-8') as f:
        ch16_original = f.read()
        
    overlap = "Meeting the Market Watchdogs"
    overlap_idx = ch16_body_english.find(overlap)
    
    if overlap_idx != -1:
        line_end = ch16_body_english.find('\n', overlap_idx)
        ch16_append = ch16_body_english[line_end+1:]
    else:
        if "Watchdogs" in ch16_body_english:
             overlap_idx = ch16_body_english.find("Watchdogs")
             line_end = ch16_body_english.find('\n', overlap_idx)
             ch16_append = ch16_body_english[line_end+1:]
        else:
             ch16_append = ch16_body_english
        
    with open('SIE Exam 20252026 For Dummies/ch16_questions_translated.md', 'r', encoding='utf-8') as f:
        ch16_questions = f.read()
        
    final_ch16 = ch16_original + "\n\n" + ch16_append + "\n\n" + ch16_questions
    
    with open('SIE Exam 20252026 For Dummies/chapter16_bilingual.md', 'w', encoding='utf-8') as f:
        f.write(final_ch16)

    print("Assembly complete.")

if __name__ == "__main__":
    assemble_ch15_16()
