# CLAUDE.md - SIE Exam Study Repository

This repository contains comprehensive study materials for the Securities Industry Essentials (SIE) exam, a financial industry qualification exam administered by FINRA. The repository is organized for systematic exam preparation with bilingual (Chinese-English) resources.

## Repository Structure

### Core Study Materials
- **`SIE考试最全集合指南-柜台与交易研发部.md`** - Comprehensive exam guide covering background, study methods, resources, and preparation strategies
- **`SIE考试备考计划（2-3个月，12周）.md`** - Detailed 12-week study plan with daily schedules and practice strategies
- **`20251018.md`** - Practice questions with detailed explanations (23 questions covering key exam topics)
- **`SIE Exam 20252026 For Dummies/`** - Main textbook and supplementary materials

### Key Directories
- `SIE Exam 20252026 For Dummies/` - Primary study materials including:
  - Full textbook PDF
  - Part-by-part study materials (PDF and DOCX)
  - Practice exams and supplementary content

## Exam Overview

### SIE Exam Basics
- **Exam Duration**: 105 minutes
- **Questions**: 85 total (10 experimental, 75 scored)
- **Passing Score**: ~70% (FINRA determined)
- **Exam Language**: English
- **Validity**: 4 years

### Content Areas
1. **Knowledge of Capital Markets** (16%) - Market structure, participants, primary/secondary markets
2. **Understanding Products and Their Risks** (44%) - Stocks, bonds, funds, options, derivatives
3. **Trading, Customer Accounts, and Prohibited Activities** (31%) - Order types, margin, suitability, regulations
4. **Overview of Regulatory Framework** (9%) - SEC, FINRA, MSRB, compliance

## Study Resources

### Primary Materials
- **For Dummies Textbook**: Complete coverage of all exam topics
- **Practice Questions**: 23 detailed questions with bilingual explanations
- **Study Plans**: Structured 12-week preparation schedule
- **Exam Strategies**: Test-taking techniques and time management

### Supplementary Resources
- Official FINRA practice test
- Online video courses and tutorials
- Flashcards and memory aids
- Regulatory framework summaries

## Common Operations

### Study Session Management
```bash
# Review specific exam topics
grep -r "ETF" . --include="*.md"

# Practice question analysis
cat 20251018.md | grep -A 20 "# 1."

# Study plan tracking
cat "SIE考试备考计划（2-3个月，12周）.md" | head -50
```

### Resource Navigation
```bash
# Find specific content in study guides
grep -n "mutual fund" "SIE考试最全集合指南-柜台与交易研发部.md"

# Access textbook sections
ls "SIE Exam 20252026 For Dummies/"

# Review practice questions by topic
grep "Correct" 20251018.md | head -10
```

### Progress Tracking
```bash
# Check completed practice questions
grep -c "Correct正确" 20251018.md

# Review study schedule
cat "SIE考试备考计划（2-3个月，12周）.md" | grep -A 5 "第1周"
```

## Key Concepts and Terminology

### Financial Products
- **ETFs vs Mutual Funds**: Expense ratios, tax efficiency, trading mechanisms
- **Bonds**: Price-yield relationships, current yield vs YTM
- **Options**: Calls, puts, intrinsic value, time value
- **REITs**: Real estate investment trusts, cash flow focus

### Regulatory Framework
- **SEC**: Securities and Exchange Commission (1934 Act)
- **FINRA**: Financial Industry Regulatory Authority (SRO)
- **MSRB**: Municipal Securities Rulemaking Board
- **Investment Company Act 1940**: Mutual fund registration

### Market Structure
- **Primary vs Secondary Markets**: Issuance vs trading
- **Bid-Ask Spread**: Market maker compensation
- **Order Types**: Market, limit, stop, stop-limit
- **Settlement**: T+2 for stocks, T+1 for options

## Study Strategies

### Effective Learning Methods
1. **Spaced Repetition**: Use practice questions with interval review
2. **Active Recall**: Test knowledge without reference materials
3. **Concept Mapping**: Connect related topics across domains
4. **Bilingual Review**: Leverage both Chinese and English explanations

### Exam Preparation Tips
- Focus on high-weightage sections (Products & Risks: 44%)
- Master regulatory timeframes and thresholds
- Practice with official FINRA sample questions
- Use the 12-week study plan for structured preparation

## Repository Navigation Tips

### Quick Reference Commands
```bash
# Find all practice questions about a specific topic
grep -B 5 -A 15 "ETF" 20251018.md

# Check study progress against weekly targets
grep "第8周" "SIE考试备考计划（2-3个月，12周）.md"

# Review regulatory framework content
grep -A 10 "监管框架" "SIE考试最全集合指南-柜台与交易研发部.md"
```

### Content Discovery
- Use `grep` with Chinese keywords for specific content
- Leverage the bilingual nature for concept clarification
- Follow the structured study plan for systematic preparation
- Reference practice questions for exam-style preparation

## Maintenance and Updates

This repository is maintained as a comprehensive SIE exam preparation resource. Future updates may include:
- Additional practice questions
- Updated regulatory information
- Enhanced study strategies
- New exam preparation techniques

---

*This CLAUDE.md file provides guidance for navigating and utilizing the SIE exam study repository effectively. The repository contains all necessary materials for comprehensive exam preparation with bilingual support.*