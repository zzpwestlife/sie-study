import re
import csv
import os

# --- Configuration ---
GLOSSARY_PATH = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/术语对照表.md"
CHAPTER_PATH = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/chapter5_bilingual.md"
LOG_PATH = "/Users/joeyzou/Code/OpenSource/sie-study/SIE Exam 20252026 For Dummies/chapter5_proofreading_log.csv"

NEW_TERMS = [
    {"en": "Competitive Offering", "cn": "竞价发行", "def": "发行人通过投标程序选择承销商的发行方式。", "ex": "Municipal bonds are often sold through a competitive offering."},
    {"en": "Funded Debt", "cn": "长期债务", "def": "期限通常在一年以上的公司债务。", "ex": "Funded debt refers to corporate liabilities with a maturity of more than one year."},
    {"en": "Investment Banking Firm", "cn": "投资银行", "def": "协助发行人筹集资金并提供并购建议的金融机构。", "ex": "Investment banking firms help issuers raise money."},
    {"en": "Managing Underwriter", "cn": "管理承销商", "def": "负责组建承销团并与发行人直接对接的主承销商。", "ex": "The managing underwriter receives financial compensation for every share sold."},
    {"en": "Negotiated Offering", "cn": "议价发行", "def": "发行人直接选择承销商并协商发行条款的发行方式。", "ex": "Corporate issues are typically sold through a negotiated offering."},
    {"en": "Red Herring", "cn": "红鲱鱼", "def": "初步招股说明书的俗称，因封面有红色免责声明而得名。", "ex": "A preliminary prospectus is sometimes called a red herring."},
    {"en": "Standby Underwriting", "cn": "备用承销", "def": "承销商承诺购买配股发行中股东未认购股份的承销方式。", "ex": "A standby underwriter agrees to purchase any stock not purchased by the public."},
    {"en": "Underwriting Agreement", "cn": "承销协议", "def": "发行人与承销商之间签署的规定发行条款的合同。", "ex": "The underwriting agreement is signed before securities can be sold."},
    {"en": "Unfunded Debt", "cn": "短期债务", "def": "期限在一年以内的短期债务。", "ex": "Unfunded debt consists of short-term liabilities."}
]

# --- Step 1: Update Glossary ---
print("Updating Glossary...")
with open(GLOSSARY_PATH, 'r', encoding='utf-8') as f:
    glossary_content = f.read()

# Split into table and footer (Abbreviations)
if "## 常见缩写" in glossary_content:
    table_part, footer_part = glossary_content.split("## 常见缩写", 1)
    footer_part = "## 常见缩写" + footer_part
else:
    table_part = glossary_content
    footer_part = ""

lines = table_part.splitlines()
header_lines = []
table_lines = []
for line in lines:
    if line.strip().startswith('|'):
        if "---" in line:
            header_lines.append(line)
        elif "英文术语" in line:
            header_lines.append(line)
        else:
            table_lines.append(line)
    else:
        header_lines.append(line)

# Parse existing table lines to avoid duplicates
existing_terms = set()
parsed_table_rows = []

for line in table_lines:
    parts = [p.strip() for p in line.split('|')]
    if len(parts) >= 3:
        term = parts[1].replace("**", "").strip()
        existing_terms.add(term.lower())
        parsed_table_rows.append(line)

# Add new terms
for term in NEW_TERMS:
    if term["en"].lower() not in existing_terms:
        new_row = f"| **{term['en']}** | {term['cn']} | {term['def']} | {term['ex']} |"
        parsed_table_rows.append(new_row)
        print(f"Added: {term['en']}")

# Sort table rows by English term
parsed_table_rows.sort(key=lambda x: x.split('|')[1].replace("**", "").strip().lower())

# Reconstruct Glossary
new_glossary_content = "\n".join(header_lines).strip() + "\n" + "\n".join(parsed_table_rows) + "\n\n" + footer_part.strip() + "\n"

with open(GLOSSARY_PATH, 'w', encoding='utf-8') as f:
    f.write(new_glossary_content)

print("Glossary Updated.")

# --- Step 2: Proofread Chapter 5 ---
print("Proofreading Chapter 5...")
with open(CHAPTER_PATH, 'r', encoding='utf-8') as f:
    chapter_lines = f.readlines()

log_entries = []
new_chapter_lines = []
previous_line_en = ""

# Helper to fix punctuation
def fix_punctuation(text):
    original = text
    # Replace parens
    text = text.replace("(", "（").replace(")", "）")
    # Restore English/Number parens if needed (but user said NO half-width in Chinese lines except numbers)
    # However, things like "1." or "A." or "IPO" might be tricky.
    # User said: "中文段落内禁止使用半角标点，数字与百分号使用半角".
    # So (A) -> （A） is correct.
    # (IPO) -> （IPO） is correct.
    # (1) -> （1）? User said "数字...使用半角". But usually parens around numbers are full-width in Chinese.
    # Let's assume standard Chinese punctuation rules: （1）.
    
    # Replace brackets
    text = text.replace("[", "［").replace("]", "］")
    
    # Replace specific terminology issues
    # Funded/Unfunded Debt
    if "有担保（长期）债务" in text:
        text = text.replace("有担保（长期）债务", "长期债务（Funded Debt）")
    if "无担保（短期）债务" in text:
        text = text.replace("无担保（短期）债务", "短期债务（Unfunded Debt）")
        
    return text

# Identify Chinese lines:
# Heuristic: If line contains Chinese characters.
# OR: Based on alternating structure.
# Structure: En, Cn, Empty.
# But sometimes headers, lists, etc.
# Safest: Detect Chinese characters.

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

for i, line in enumerate(chapter_lines):
    line_stripped = line.strip()
    original_line = line
    
    if not line_stripped:
        new_chapter_lines.append(line)
        continue
        
    # Check if this line is likely a Chinese translation line
    # (Contains Chinese)
    if has_chinese(line):
        # Proofread this line
        revised_line = fix_punctuation(line)
        
        # Specific terminology checks (Strings to Strings)
        # Note: fix_punctuation already did Funded Debt.
        
        if revised_line != original_line:
            reason = "Punctuation/Format/Terminology"
            if "Funded Debt" in revised_line and "Funded Debt" not in original_line:
                reason = "Terminology Correction (Funded Debt)"
            
            # Remove newline for CSV
            cn_orig = original_line.strip()
            cn_rev = revised_line.strip()
            
            # Find corresponding English text (likely the previous non-empty line)
            # We need to look back.
            en_text = "N/A"
            # Look backwards from i-1
            k = i - 1
            while k >= 0:
                if chapter_lines[k].strip() and not has_chinese(chapter_lines[k]):
                    en_text = chapter_lines[k].strip()
                    break
                k -= 1
            
            log_entries.append({
                "Paragraph_ID": i + 1,
                "EN_Text": en_text[:50] + "..." if len(en_text) > 50 else en_text,
                "CN_Original": cn_orig,
                "CN_Revised": cn_rev,
                "Reason": reason,
                "Glossary_Source": "术语对照表.md"
            })
            
            new_chapter_lines.append(revised_line)
        else:
            new_chapter_lines.append(line)
    else:
        # English line or code or empty
        new_chapter_lines.append(line)

# Write Log
print("Writing Log...")
with open(LOG_PATH, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Paragraph_ID", "EN_Text", "CN_Original", "CN_Revised", "Reason", "Glossary_Source"])
    writer.writeheader()
    writer.writerows(log_entries)

# Write Updated Chapter
print("Writing Chapter...")
with open(CHAPTER_PATH, 'w', encoding='utf-8') as f:
    f.writelines(new_chapter_lines)

print("Done.")
