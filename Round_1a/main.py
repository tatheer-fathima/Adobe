import fitz  # PyMuPDF
import os
import json

def extract_headings_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = ""

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    text = "".join([span["text"] for span in line["spans"]]).strip()
                    if not text or len(text) < 3:
                        continue
                    font_size = line["spans"][0]["size"]
                    font_flags = line["spans"][0]["flags"]

                    # Heuristic rules
                    if page_num == 0 and font_size > 15:
                        title = text

                    heading_level = None
                    if font_size > 13:
                        heading_level = "H1"
                    elif font_size > 11:
                        heading_level = "H2"
                    elif font_size > 10:
                        heading_level = "H3"

                    if heading_level:
                        outline.append({
                            "level": heading_level,
                            "text": text,
                            "page": page_num + 1
                        })

    return {
        "title": title if title else "Untitled Document",
        "outline": outline
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            result = extract_headings_from_pdf(os.path.join(input_dir, file))
            with open(os.path.join(output_dir, file.replace(".pdf", ".json")), "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()