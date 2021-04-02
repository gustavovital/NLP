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

# Declarar a pasta com os arquivos Pdfs a serem lidos:
DataPath = "Data/"  # se estiver na pasta raiz, deixar só duas aspas: ""

# Cria um lista vazia pdfFiles: o glob vai armazenar todos os arquivos em pdf
# nessa lista.
pdfFiles = []
for file in glob.glob("{}*.pdf".format(DataPath)):
    pdfFiles.append(file)

# Função que realiza leitura do pdf a partir do modulo PyPDF2:


def readPDF(file):

    with open(file, "rb") as pdfFile:

        readPdf = PyPDF2.PdfFileReader(pdfFile)
        numberOfPages = readPdf.getNumPages()
        text = ""

        for pageNumber in range(numberOfPages):
            page = readPdf.getPage(pageNumber)
            pageContent = page.extractText()
            text += pageContent

    text = text.replace("\n", "")

    return text

# Lendo todos os pdfs de uma pasta, por exemplo:

for file in pdfFiles:
    print(readPDF(file))

# Definindo uma função para criação de corpus


def createCorpus(Files):  # files tem que estar em formato de lista

    names = []
    try:
        index =
        for file in Files:

            print(file)
    except TypeError:
        print("O argumento da função tem que ser uma lista.")

createCorpus(pdfFiles)
