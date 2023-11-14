'''python file that showcase how to merge two PDFs'''
import os
# import sys
import PyPDF2

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined_pdf.pdf")
