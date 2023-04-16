from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re

pdf_path = "PDF\The_Land_of_Dragons_Dungeons.pdf"
pdf_text = ""

# Extract text page by page
with open(pdf_path, 'rb') as file:
    for element in page:
        if isinstance(element, LTTextContainer):
            pdf_text += element.get_text()

# Proceed with data preprocessing steps
# Step 1: Text extraction from PDF


# Step 2: Data preprocessing

# 2.1. Remove line breaks and replace them with spaces
pdf_text = pdf_text.replace('\n', ' ')

# 2.2. Remove multiple spaces and special characters
pdf_text = re.sub(r'\s+', ' ', pdf_text)
pdf_text = re.sub(r'\W+', ' ', pdf_text)

# Tokenize text into sentences
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', pdf_text)

print(sentences)