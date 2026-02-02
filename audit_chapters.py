import os
import re
import glob

# Configuration
CHAPTER_DIR = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies"
SOURCE_FILES = {
    "part2": f"{CHAPTER_DIR}/part2 basic security investments_extracted.txt",
    "part3": f"{CHAPTER_DIR}/part3 more complex securities_extracted.txt",
    "part4": f"{CHAPTER_DIR}/part4 client needs and rules_extracted.txt"
}

# Chapter to Part Mapping (Heuristic based on book structure)
# Ch 5-8: Part 2
# Ch 9-11: Part 3
# Ch 12-16: Part 4
CHAPTER_MAP = {
    5: "part2", 6: "part2", 7: "part2", 8: "part2",
    9: "part3", 10: "part3", 11: "part3",
    12: "part4", 13: "part4", 14: "part4", 15: "part4", 16: "part4"
}

def count_questions_in_text(text, chapter_num):
    # Locate chapter start
    # Pattern: "Chapter X" or "CHAPTER X"
    # Locate "Testing Your Knowledge" or "Practice questions"
    # Count numbered items 1. 2. 3. ...
    
    # Clean text: remove newlines in middle of sentences to make regex easier?
    # Or just scan line by line.
    
    lines = text.split('\n')
    in_chapter = False
    in_quiz = False
    questions = []
    
    # Regex for Chapter Header: "Chapter 12" or "CHAPTER 12"
    # Note: PDF extraction might put spaces or symbols: "C H A P T E R  1 2"
    
    # Simplified: Find the index of "Chapter X" and "Chapter X+1"
    # Then search for "Practice questions" within that range.
    
    # Let's find all "Practice questions" or "Testing Your Knowledge" occurrences
    # and associate them with the nearest preceding "Chapter X".
    
    chapter_starts = []
    for i, line in enumerate(lines):
        # Flexible matching for "Chapter X"
        if re.search(rf'^\s*CHAPTER\s*{chapter_num}\b', line, re.IGNORECASE):
            chapter_starts.append(i)
        # Check for title case "Chapter 5"
        elif re.search(rf'^\s*Chapter\s*{chapter_num}\b', line):
            chapter_starts.append(i)
            
    if not chapter_starts:
        return 0, "Chapter start not found in source"
        
    # Assume the last valid start is the real one (sometimes TOC has it too)
    # But wait, TOC is usually at the beginning.
    # Let's pick the one followed by title text.
    
    start_idx = chapter_starts[-1] 
    
    # Find end of chapter (Next Chapter or Part End)
    end_idx = len(lines)
    next_chapter_num = chapter_num + 1
    for i in range(start_idx + 100, len(lines)):
        if re.search(rf'^\s*CHAPTER\s*{next_chapter_num}\b', line, re.IGNORECASE) or \
           re.search(rf'^\s*Chapter\s*{next_chapter_num}\b', line):
            end_idx = i
            break
            
    chapter_text = lines[start_idx:end_idx]
    
    # Find "Testing Your Knowledge" or "Practice questions"
    quiz_start = -1
    for i, line in enumerate(chapter_text):
        if "Testing Your Knowledge" in line or "Practice questions" in line:
            quiz_start = i
            # Don't break immediately, find the last occurrence (sometimes header repeats)
            # Actually, usually it's at the end.
            
    if quiz_start == -1:
        return 0, "Quiz section not found"
        
    quiz_text = chapter_text[quiz_start:]
    
    # Count questions: Look for "1.", "2.", etc. at start of line
    # Or "10."
    max_q = 0
    for line in quiz_text:
        match = re.match(r'^\s*(\d+)\.', line)
        if match:
            q_num = int(match.group(1))
            # Sequence check: usually 1, 2, 3...
            # If we jump from 1 to 10, it's an error.
            if q_num == max_q + 1:
                max_q = q_num
            elif q_num > max_q and q_num < max_q + 5: # Allow small gaps or OCR errors? No, strict.
                 # Maybe some questions span lines and we missed one?
                 # Let's just track the highest number found that follows sequence roughly.
                 pass
    
    # Try a more robust approach: Find all "N." patterns
    q_nums = []
    for line in quiz_text:
        match = re.match(r'^\s*(\d+)\.', line)
        if match:
            q_nums.append(int(match.group(1)))
            
    # Filter for a logical sequence 1..N
    if not q_nums:
        return 0, "No numbered questions found"
        
    q_nums = sorted(list(set(q_nums)))
    # Ensure it starts at 1
    if 1 not in q_nums:
        return 0, "Questions do not start at 1"
        
    # Find longest consecutive sequence starting at 1
    count = 0
    for i in range(1, max(q_nums) + 2):
        if i in q_nums:
            count = i
        else:
            break
            
    return count, "OK"

def count_questions_in_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Look for "Practice questions" section
    if "Practice questions" not in content and "Testing Your Knowledge" not in content:
        return 0
        
    # Regex for "1." "2." etc
    # In MD, it might be "1. " or "10. "
    matches = re.findall(r'^\s*(\d+)\.', content, re.MULTILINE)
    if not matches:
        return 0
        
    nums = sorted(list(set(map(int, matches))))
    
    # Filter out potential TOC numbers (usually small) if they are not in the quiz section?
    # The quiz is usually at the end.
    # Let's split by "Practice questions"
    parts = re.split(r'Practice questions|Testing Your Knowledge', content)
    if len(parts) < 2:
        return 0
    
    quiz_content = parts[-1]
    matches = re.findall(r'^\s*(\d+)\.', quiz_content, re.MULTILINE)
    if not matches:
        return 0
        
    nums = sorted(list(set(map(int, matches))))
    
    count = 0
    for i in range(1, max(nums) + 2):
        if i in nums:
            count = i
        else:
            break
    return count

def main():
    print(f"{'Chapter':<10} | {'Source (PDF)':<12} | {'Target (MD)':<12} | {'Status':<10}")
    print("-" * 50)
    
    discrepancies = []
    
    for ch_num in range(5, 17):
        md_file = f"{CHAPTER_DIR}/chapter{ch_num}_bilingual.md"
        
        if not os.path.exists(md_file):
            print(f"Chapter {ch_num:<2} | {'N/A':<12} | {'Missing':<12} | ERROR")
            continue
            
        # Get Source Count
        part_key = CHAPTER_MAP.get(ch_num)
        source_txt_path = SOURCE_FILES.get(part_key)
        
        if not source_txt_path or not os.path.exists(source_txt_path):
             print(f"Chapter {ch_num:<2} | {'No Source':<12} | {'?':<12} | SKIP")
             continue
             
        with open(source_txt_path, 'r', encoding='utf-8') as f:
            source_text = f.read()
            
        src_count, msg = count_questions_in_text(source_text, ch_num)
        
        # Get Target Count
        tgt_count = count_questions_in_md(md_file)
        
        status = "MATCH" if src_count == tgt_count else "MISMATCH"
        print(f"Chapter {ch_num:<2} | {src_count:<12} | {tgt_count:<12} | {status}")
        
        if status == "MISMATCH":
            discrepancies.append((ch_num, src_count, tgt_count))
            
    # Save discrepancies to file for next step
    with open("audit_results.txt", "w") as f:
        for item in discrepancies:
            f.write(f"{item[0]},{item[1]},{item[2]}\n")

if __name__ == "__main__":
    main()
