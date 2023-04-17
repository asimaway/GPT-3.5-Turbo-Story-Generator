import os
from docx import Document
from docx2pdf import convert

def find_next_available_filename(folder, filename_base, extension):
    index = 1
    while os.path.exists(os.path.join(folder, f"{filename_base}_{index:03}.{extension}")):
        index += 1
    return os.path.join(folder, f"{filename_base}_{index:03}.{extension}")

def save_as_docx(folder, filename_base, story):
    extension = "docx"
    available_filename = find_next_available_filename(folder, filename_base, extension)

    document = Document()
    document.add_paragraph(story)
    document.save(available_filename)
    
    return available_filename

def save_as_pdf(folder, filename_base, story):
    docx_filename = save_as_docx(folder, filename_base, story)
    pdf_filename = os.path.splitext(docx_filename)[0] + ".pdf"
    convert(docx_filename, pdf_filename)

    return pdf_filename
