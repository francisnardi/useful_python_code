from pdf2docx import Converter
pdf_file = 'pdf-test.pdf'
docx_file = 'pdf-test.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
