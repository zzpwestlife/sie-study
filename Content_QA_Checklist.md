# Content QA Checklist for SIE Study Materials

This checklist establishes the standard for reviewing and validating the completeness and quality of SIE exam study materials.

## 1. Structural Integrity
- [ ] **File Naming**: Follows `chapterX_bilingual.md` format.
- [ ] **TOC**: Includes `[TOC]` marker or clear Table of Contents.
- [ ] **Headings**: Proper hierarchy (# Chapter, ## Section, ### Subsection).
- [ ] **Bilingual Format**:
  - [ ] English paragraph followed by Chinese paragraph.
  - [ ] Empty line separating language blocks.
  - [ ] No mixed-language paragraphs (except specific terms).

## 2. Core Content Elements
- [ ] **Introduction**: Chapter overview present.
- [ ] **Main Body**: All sections from source PDF/Textbook included.
- [ ] **Key Concepts**: "Remember" (🧠), "Tip" (💡), "Example" (📝) blocks properly formatted and translated.
- [ ] **Tables/Charts**: All tables from source included and formatted in Markdown.
- [ ] **Terminology**: 
  - [ ] Consistent with `术语对照表.md`.
  - [ ] Key English terms preserved in brackets or bold.

## 3. Practice Questions (Crucial Check)
- [ ] **Quantity Check**: Compare question count with source PDF (end of chapter).
- [ ] **Content**:
  - [ ] Questions text complete.
  - [ ] Options (A, B, C, D) complete.
  - [ ] Formatting consistent (English only or Bilingual as per file standard).
- [ ] **Answers**:
  - [ ] Answer key present.
  - [ ] Explanations included and match question count.

## 4. Formatting & Mechanics
- [ ] **Punctuation**: 
  - [ ] Chinese text uses full-width punctuation (，。：).
  - [ ] Numbers/English within Chinese use half-width punctuation.
- [ ] **Line Breaks**: No broken sentences or orphan lines.
- [ ] **Encoding**: File is UTF-8 without garbled characters.

## 5. Verification Steps
1. **Source Comparison**: Open source PDF and verify section by section.
2. **Question Count**: Explicitly count "Testing Your Knowledge" items.
3. **Glossary Scan**: Run terminology check script.
