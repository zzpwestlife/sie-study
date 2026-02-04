# Project: SIE Study Guide Bilingual Documentation Completion

## Goal
Complete bilingual (English-Chinese) Markdown documentation for Chapters 6 through 16 of the SIE study guide with 100% content parity.

## Context
- Source: `Chapters_translate/Chapter_6.pdf` to `Chapter_16.pdf`
- Target: `Chapters_translate/chapter6_bilingual.md` to `chapter16_bilingual.md`
- Requirement: `[English] \n [Chinese]` format, 100% parity, technical financial accuracy.
- Current Status: Files exist but are inconsistent in length (e.g., Chapter 14 is very short while Chapter 15 is long).

## Tech Stack
- PDF processing: `look_at` (if authorized), `omo-agent`
- Translation: `ultrabrain` (omo-agent), LLM-based translation
- Documentation: Markdown
- Verification: `explore` agent

## Key Files
- `Chapters_translate/翻译要求.md`: Translation standards
- `Chapters_translate/术语对照表.md`: Glossary
