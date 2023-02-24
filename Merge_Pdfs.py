import PyPDF2
import os

pdfFiles = []
for filename in os.listdir("./Sample Pdfs"):
    if filename.endswith(".pdf") and filename != "merged.pdf":
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfMerger = PyPDF2.PdfMerger()

for filename in pdfFiles:
    pdfFile = open(f"./Sample Pdfs/{filename}", "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerger.append(pdfReader)
    pdfFile.close()

pdfMerger.write("./Sample Pdfs/merged.pdf")
print("Merging completed")
