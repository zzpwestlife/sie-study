
def assemble_ch14():
    with open('SIE Exam 20252026 For Dummies/chapter14_bilingual_fixed.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find line with "## 7. Testing Your Knowledge"
    limit_idx = 0
    for i, line in enumerate(lines):
        if "## 7. Testing Your Knowledge" in line:
            limit_idx = i
            break
            
    if limit_idx == 0:
        print("Could not find '## 7. Testing Your Knowledge'")
        return

    content_base = "".join(lines[:limit_idx])
    
    with open('SIE Exam 20252026 For Dummies/ch14_questions_translated.md', 'r', encoding='utf-8') as f:
        content_questions = f.read()
        
    final_content = content_base + content_questions
    
    with open('SIE Exam 20252026 For Dummies/chapter14_bilingual.md', 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Chapter 14 assembled. Length: {len(final_content)}")

if __name__ == "__main__":
    assemble_ch14()
