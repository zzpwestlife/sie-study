
import re

def split_chapters():
    with open('SIE Exam 20252026 For Dummies/chapter14_bilingual.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find Chapter headers
    # Note: The file likely contains "CHAPTER 15" and "CHAPTER 16" in all caps based on my Read output
    # or "Chapter 15" etc.
    # My read output showed "CHAPTER 15 Making Sure the IRS..."
    # and "CHAPTER 16 Rules and Regulations..."
    
    # Let's find the indices
    match_15 = re.search(r'CHAPTER\s+15\s+Making\s+Sure', content, re.IGNORECASE)
    match_16 = re.search(r'CHAPTER\s+16\s+Rules\s+and', content, re.IGNORECASE)

    if not match_15:
        print("Could not find Chapter 15 start")
        return
    
    idx_15 = match_15.start()
    
    if match_16:
        idx_16 = match_16.start()
    else:
        print("Could not find Chapter 16 start, assuming rest is Ch 15")
        idx_16 = len(content)

    ch14_content = content[:idx_15]
    ch15_content = content[idx_15:idx_16]
    ch16_content = content[idx_16:]

    with open('SIE Exam 20252026 For Dummies/chapter14_bilingual_fixed.md', 'w', encoding='utf-8') as f:
        f.write(ch14_content)
    
    with open('SIE Exam 20252026 For Dummies/temp_ch15_english.md', 'w', encoding='utf-8') as f:
        f.write(ch15_content)
        
    with open('SIE Exam 20252026 For Dummies/temp_ch16_english.md', 'w', encoding='utf-8') as f:
        f.write(ch16_content)

    print(f"Split complete.")
    print(f"Ch 14 length: {len(ch14_content)}")
    print(f"Ch 15 length: {len(ch15_content)}")
    print(f"Ch 16 length: {len(ch16_content)}")

if __name__ == "__main__":
    split_chapters()
