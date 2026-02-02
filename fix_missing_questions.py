import re
import os

source_file = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/part4 client needs and rules_extracted.txt"
ch14_md = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/chapter14_bilingual.md"
ch15_md = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/chapter15_bilingual.md"
ch16_md = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/chapter16_bilingual.md"

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

lines = read_file(source_file)

def clean_lines(lines):
    cleaned = []
    for line in lines:
        l = line.strip()
        # Remove arrow chars or page numbers if present (e.g. 2143→)
        l = re.sub(r'^\d+→', '', l)
        l = l.replace('→', '')
        if l:
            cleaned.append(l)
    return cleaned

def append_to_file(path, content):
    with open(path, 'a', encoding='utf-8') as f:
        f.write("\n\n" + content + "\n")

# --- Chapter 14 ---
# Questions 9-15
ch14_q_start_idx = -1
for i in range(2100, 2200):
    if "9. Which of the following order features" in lines[i]:
        ch14_q_start_idx = i
        break

ch14_q_end_idx = -1
for i in range(ch14_q_start_idx, 2200):
    if "Answers and explanations" in lines[i]:
        ch14_q_end_idx = i
        break

ch14_questions = lines[ch14_q_start_idx:ch14_q_end_idx]

# Answers for 9-15
ch14_a_start_idx = -1
for i in range(ch14_q_end_idx, 2300):
    if "9. C." in lines[i]: 
        ch14_a_start_idx = i
        break

ch14_a_end_idx = -1
for i in range(ch14_a_start_idx, 2300):
    if "CHAPTER" in lines[i] and "15" in lines[i]:
        ch14_a_end_idx = i
        break

ch14_answers = lines[ch14_a_start_idx:ch14_a_end_idx]

q14_clean = clean_lines(ch14_questions)
a14_clean = clean_lines(ch14_answers)
# Fix Q11 text
for idx, l in enumerate(q14_clean):
    if "11. Which of the following order features allows for partial execution?" in l:
        q14_clean[idx] = "11. A market maker quotes a stock at 18.10 - 18.30, 20 x 25. This means the market maker is willing to:"

content14 = "### Additional Practice Questions\n\n" + "\n".join(q14_clean) + "\n\n### Additional Answers\n\n" + "\n".join(a14_clean)
print(f"Appending to Ch 14: {len(q14_clean)} lines of Qs")
append_to_file(ch14_md, content14)


# --- Chapter 15 ---
# Missing Source Q5, Q6, Q7, Q9.
ch15_q_start_idx = -1
for i in range(2700, 2800):
    if "5. An individual investor" in lines[i]:
        ch15_q_start_idx = i
        break

ch15_q_end_idx = -1
for i in range(ch15_q_start_idx, 2800):
    if "Answers and explanations" in lines[i]:
        ch15_q_end_idx = i
        break

ch15_questions_raw = lines[ch15_q_start_idx:ch15_q_end_idx]
ch15_questions_filtered = []
skip = False
for line in ch15_questions_raw:
    if "8. According to the wash sale rule" in line:
        skip = True
    if "9. Which of the following" in line:
        skip = False
    if not skip:
        ch15_questions_filtered.append(line)

# Answers
ch15_a_start_idx = -1
for i in range(ch15_q_end_idx, 2900):
    if "5. A." in lines[i] or "5. A" in lines[i]:
        ch15_a_start_idx = i
        break

ch15_a_end_idx = -1
for i in range(ch15_a_start_idx, 2900):
    if "CHAPTER" in lines[i] and "16" in lines[i]:
        ch15_a_end_idx = i
        break

ch15_answers_raw = lines[ch15_a_start_idx:ch15_a_end_idx]
ch15_answers_filtered = []
skip = False
for line in ch15_answers_raw:
    if "8. A." in line:
        skip = True
    if "9. C." in line:
        skip = False
    if not skip:
        ch15_answers_filtered.append(line)

q15_clean = clean_lines(ch15_questions_filtered)
a15_clean = clean_lines(ch15_answers_filtered)
content15 = "### Additional Practice Questions\n\n" + "\n".join(q15_clean) + "\n\n### Additional Answers\n\n" + "\n".join(a15_clean)
print(f"Appending to Ch 15: {len(q15_clean)} lines of Qs")
append_to_file(ch15_md, content15)


# --- Chapter 16 ---
# Questions 7-25
ch16_q_start_idx = -1
for i in range(len(lines) - 1000, len(lines)):
    if "7. Which of the following is an indication" in lines[i]:
        ch16_q_start_idx = i
        break

ch16_q_end_idx = -1
for i in range(ch16_q_start_idx, len(lines)):
    if "Answers and explanations" in lines[i]:
        ch16_q_end_idx = i
        break

ch16_questions = lines[ch16_q_start_idx:ch16_q_end_idx]

# Answers 7-25
ch16_a_start_idx = -1
for i in range(ch16_q_end_idx, len(lines)):
    if "7. D." in lines[i]:
        ch16_a_start_idx = i
        break

ch16_a_end_idx = len(lines)

ch16_answers = lines[ch16_a_start_idx:ch16_a_end_idx]

q16_clean = clean_lines(ch16_questions)
a16_clean = clean_lines(ch16_answers)
content16 = "### Additional Practice Questions\n\n" + "\n".join(q16_clean) + "\n\n### Additional Answers\n\n" + "\n".join(a16_clean)
print(f"Appending to Ch 16: {len(q16_clean)} lines of Qs")
append_to_file(ch16_md, content16)
