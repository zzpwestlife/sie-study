import os
import sys
import re

# Ensure PyMuPDF is available
try:
    import fitz  # PyMuPDF
except Exception:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyMuPDF'])
    import fitz

# Determine PDF path (prefer annotated copy)
workspace = os.getcwd()
pdf_candidates = [
    os.path.abspath(os.path.join(workspace, 'ForDummies_dual_annotated_20251018.pdf')),
    os.path.abspath(os.path.join(workspace, '中英对照版-SIE Exam 20252026 For Dummies (Securities Industry Essentials Exam Prep + Practice Tests  Flashcards Online), 4th (Steven M. Rice) _dual.pdf')),
]

pdf_path = None
for p in pdf_candidates:
    if os.path.exists(p):
        pdf_path = p
        break

if not pdf_path:
    print('ERROR: PDF not found in workspace. Check filenames.')
    sys.exit(1)

# Q8-related keywords (English + Chinese)
kw_en = [
    'no-load', 'no load',
    'sales charge', 'front-end load', 'back-end load', 'backend load',
    'contingent deferred sales charge', 'cdsc',
    '12b-1', '12 b-1', '12 b 1', '12b1', '12-1', '12 1',
    'basis points', 'bps', '0.25%', '25 basis points', '25 bps',
    '0.75%', '75 basis points', '75 bps',
    'class a shares', 'class b shares', 'class c shares',
    'expense ratio', 'distribution fee', 'service fee'
]

kw_zh = [
    '无销售费', '零销售费', '销售费用',
    '前端销售费', '后端销售费', '延期销售费', '有条件延期销售费',
    'CDSC', '12b-1费用', '12-1费用',
    '基点', '25个基点', '75个基点', '0.75%', '0.25%',
    '费用比率', '分销费', '服务费',
    'A类份额', 'B类份额', 'C类份额'
]

keywords = list(dict.fromkeys(kw_en + kw_zh))  # dedupe, keep order

print(f'Using PDF: {pdf_path}')

doc = fitz.open(pdf_path)
highlighted_pages = set()

for page_index in range(doc.page_count):
    page = doc.load_page(page_index)
    page_text = page.get_text('text') or ''
    matched_any = False

    for term in keywords:
        # Try multiple case variants to improve hit rate
        variants = {term, term.lower(), term.upper(), term.title()}
        rects = []
        for v in variants:
            try:
                rects += page.search_for(v, hit_max=200)
            except Exception:
                # Fallback minimal search
                rects += page.search_for(v)
        if rects:
            matched_any = True
            for r in rects:
                try:
                    page.add_highlight_annot(r)
                except Exception:
                    pass
        else:
            # If textual match exists but no rects (hyphenation / layout), add a note
            if re.search(re.escape(term), page_text, flags=re.IGNORECASE):
                matched_any = True

    if matched_any:
        highlighted_pages.add(page_index + 1)  # 1-based
        # Tag the page with a small text annotation near top-left
        try:
            page.add_text_annot(fitz.Point(36, 36), 'Q8 keywords highlighted')
        except Exception:
            pass

# Save incremental changes if possible
try:
    doc.saveIncr()
except Exception:
    # If incremental fails, save to same path
    doc.save(pdf_path)

doc.close()

highlighted_pages_sorted = sorted(highlighted_pages)
print('Total highlighted pages:', len(highlighted_pages_sorted))
# Print up to first 40 pages for reference
preview_pages = highlighted_pages_sorted[:40]
print('Highlighted pages (first 40):', preview_pages)