# =
# Autor : gustavovital
# Data  : 01/04/2020
#
# Script para leitura de textos em .pdf
# =

# Modulos importados:
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

# Exemplo de uso da função:
 print(read_pdf_file('Data/211th.pdf'))

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

        names = [int(i) for i in names]
        data = pd.DataFrame(list(zip(names, text)),
                            columns=['Doc', 'Text'])
        data.sort_values('Doc', inplace=True)
        data.reset_index(drop=True, inplace=True)
        return data

    except TypeError:
        print("O argumento da função tem que ser uma lista de arquivos.")


# corpus = create_corpus(pdfFiles)
# corpus.to_pickle("corpus.csv")

# corpus = pd.read_pickle("corpus.csv")

# =
# Por algum motivo, tres dos pdfs nao estao sendo lidos corretamente. O corpus ainda é um corpus sujo, isso é, ainda é
# necessário passar por um dicionario de stopwords/tecnicas de analise textual. Em geral o codigo acima realiza a
# leitura sem problemas maiores de 'encoding'
# =#

