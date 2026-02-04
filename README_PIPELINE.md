
# Content Integration & HTML Output Pipeline

This project implements a pipeline to process bilingual SIE Study Guide content. It treats Word documents (`.docx`) as the authoritative source for structure and English content, and merges Chinese translations from Markdown (`.md`) files.

## Features

*   **Authoritative Parsing**: Extracts structure (headings, lists, paragraphs) from Word documents.
*   **Intelligent Merging**: Aligns Markdown translations with Word content using fuzzy matching and structure analysis.
*   **HTML Generation**: Produces semantic, responsive HTML with:
    *   Side navigation (TOC).
    *   Bilingual support (English/Chinese).
    *   Syntax highlighting (Prism.js).
    *   Math support (MathJax).
    *   PDF download links.
    *   Visual indicators for missing translations.
*   **Batch Processing**: Processes all chapters in one go.
*   **Reporting**: Generates an index page with coverage statistics (Completion Rate).

## Directory Structure

*   `Chapters_translate/`: Source files (`.docx`, `.pdf`, `.md`).
*   `pipeline/`: Python scripts.
    *   `parser.py`: Docx and Markdown parsers.
    *   `merger.py`: Content alignment and HTML generation logic.
    *   `batch.py`: Main entry point for batch processing.
*   `output/`: Generated HTML files and assets.
*   `tests/`: Unit tests.

## Usage

### Prerequisites

*   Python 3.x
*   `python-docx` library

```bash
pip install python-docx
```

### Running the Pipeline

Run the batch processor from the project root:

```bash
python3 -m pipeline.batch
```

This will:
1.  Read all `Chapter_*.docx` and corresponding `chapter*_bilingual.md` files.
2.  Merge content.
3.  Generate `output/chapter*.html`.
4.  Copy corresponding PDFs to `output/`.
5.  Generate `output/index.html` with a coverage report.

### Viewing Results

Open `output/index.html` in your browser to see the list of chapters and their translation status.

## Testing

Run unit tests:

```bash
python3 -m unittest tests/test_pipeline.py
```

## Accessibility (WCAG 2.1)

The generated HTML uses semantic tags (`<nav>`, `<main>`, `<section>`, `<h1>-<h6>`) and high-contrast colors to meet basic accessibility standards.

## Customization

*   **Templates**: Modify `pipeline/merger.py` (inside `generate_html` method) to change the HTML structure or CSS.
*   **Matching Logic**: Adjust thresholds in `pipeline/merger.py` (`ContentMerger.merge`) to tune fuzzy matching sensitivity.
