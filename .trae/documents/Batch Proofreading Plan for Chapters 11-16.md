I will perform the systematic bilingual proofreading and terminology management for Chapters 11 through 16, following the established standards.

**Phase 1: Analysis & Preparation**

1. **Content Inspection**: Read the initial sections of Chapters 11-16 to confirm file structure and identify potential terminology clusters.
2. **Script Configuration**: Update the existing `proofread_multi_chapters.py` script to target the six new files (`chapter11_bilingual.md` through `chapter16_bilingual.md`).

   * Ensure the script continues to enforce:

     * English-Chinese paragraph alternation with empty lines.

     * Punctuation normalization (full-width for text, half-width for numbers).

     * Terminology consistency against `术语对照表.md`.

     * Logging of all changes to CSV files.

**Phase 2: Automated Processing**

1. **Execution**: Run the updated Python script to process all six chapters in batch.

   * This will automatically update the Global Glossary (`术语对照表.md`) with new terms found in these chapters.

   * It will generate six individual proofreading logs (e.g., `chapter11_bilingual_proofreading_log.csv`).

**Phase 3: Semantic Verification & Refinement (The "Human" Touch)**

1. **Manual Review**: I will personally review the processed files, focusing on:

   * **Financial Nuances**: Ensuring terms like "Wash Sale" (洗售), "Margin" (融资/保证金), "Hypothecation" (抵押), "Integration" (融合/一体化) are translated accurately according to context.

   * **Regulatory Tone**: Verifying the tone of regulatory chapters (Ch 16) matches formal compliance standards (e.g., "Statutory Disqualification" as "法定取消资格").

   * **Flow & Readability**: Correcting any "machine translation" phrasing that the script cannot catch.
2. **Corrections**: Apply specific semantic fixes using `SearchReplace` where necessary.

**Phase 4: Final Deliverables**

1. **Proofread Files**: Six fully processed bilingual markdown files.
2. **Updated Glossary**: A comprehensive `术语对照表.md` covering the entire book's scope.
3. **Change Logs**: Six CSV files documenting the specific changes for audit purposes.
4. **Final Report**: A summary of the work completed, highlighting key terminology updates and compliance checks.

