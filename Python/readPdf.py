# =
# Autor : gustavovital
# Data  : 01/04/2020
#
# Script para leitura de textos em .pdf
# =

# Modules to import:
import PyPDF2
import glob
import re
import pandas as pd

# Declarar a pasta com os arquivos Pdfs a serem lidos:
DataPath = "Data/"  # se estiver na pasta raiz, deixar só duas aspas: ""

# Cria um lista vazia pdfFiles: o glob vai armazenar todos os arquivos em pdf
# nessa lista.
pdfFiles = []
for _ in glob.glob("{}*.pdf".format(DataPath)):
    pdfFiles.append(_)

# Função que realiza leitura do pdf a partir do modulo PyPDF2:


def read_pdf_file(pdf_file):

    with open(pdf_file, "rb") as pdfFile:

        read_pdf = PyPDF2.PdfFileReader(pdfFile)
        number_of_pages = read_pdf.getNumPages()
        text = ""

        for pageNumber in range(number_of_pages):
            page = read_pdf.getPage(pageNumber)
            page_content = page.extractText()
            text += page_content

    text = text.replace("\n", "")

    return text

# Lendo todos os pdfs de uma pasta, por exemplo:

# for file in pdfFiles:
#     print(readPDF(file))

# Definindo uma função para criação de corpus


def create_corpus(files):  # files tem que estar em formato de lista

    names = []
    text = []

    try:
        for file in files:
            index = file.find('\\')
            if index != -1:
                file_name = file[(index+1):]
                file_name = re.sub(r'[a-zA-Z\.]', r'', file_name)
                names.append(file_name)
            else:
                file_name = re.sub(r'[a-zA-Z\.]', r'', file)
                names.append(file_name)

            text.append(read_pdf_file(file))
            print(text)

        # data = pd.DataFrame([names, text])

    except TypeError:
        print("O argumento da função tem que ser uma lista.")


create_corpus(pdfFiles)
