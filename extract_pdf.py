
import pypdf

def extract_text(pdf_path, output_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        with open(output_path, "w", encoding="utf-8") as f:
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                f.write(f"--- Page {page_num + 1} ---\n")
                f.write(text)
                f.write("\n\n")
        print(f"Successfully extracted text to {output_path}")
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_text("sie_study_material.pdf", "extracted_text.txt")
