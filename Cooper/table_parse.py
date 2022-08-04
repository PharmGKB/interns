import camelot as cam
import PyPDF2

#Gets the name of the pdf file
input_name = input("What is the file name? (Without .pdf suffix)")
file_name = input_name + ".pdf"

#Finds the amount of pages on the pdf
file = open(file_name, 'rb')
readpdf = PyPDF2.PdfFileReader(file)
total_pages = readpdf.numPages

#Loops through the entire document and creates excel files for each table found
for i in range(1, total_pages + 1):
    #Scans page for tables
    pdf = cam.read_pdf(file_name, pages = str(i), flavor = 'stream')
    for x in range(pdf.n):
        #Creates excel file for each table
        ddf = pdf[x].df
        temp_name = input_name + "pg" + str(i) + "#" + str(x) + ".xlsx"
        ddf.to_excel(temp_name)
