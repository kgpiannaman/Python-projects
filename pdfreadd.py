import fitz  # PyMuPDF

# Specify the path to your PDF file
pdf_path = "/Users/namanbhatia/Downloads/static/gcleong.pdf"

# Open the PDF
pdf_document = fitz.open(pdf_path)

# Extract text from each page
all_text = ""
for page_num in range(len(pdf_document)):
    page = pdf_document[page_num]
    all_text += page.get_text()

# Close the PDF after extraction
pdf_document.close()

# Save the text to a file for reference (optional)
with open("gc_leong_geography_text.txt", "w", encoding="utf-8") as text_file:
    text_file.write(all_text)

print("Text extraction completed!")
