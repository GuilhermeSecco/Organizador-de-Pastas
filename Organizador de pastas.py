#Bibliotecas
import os
from tkinter.filedialog import askdirectory

#Caminho da pasta
path = askdirectory(title="Selecione uma pasta")

#Arquivos da pasta
files_list = os.listdir(path)

#Dicionário com pastas e extensões
locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".webp"],
    "Planilhas": [".csv", ".xlsx"],
    "Videos": [".mp4"],
    "GIFs": [".gif", ".mov"],
    "Textos": [".txt"],
    "Códigos": [".ipynb"],
    "Documentos": [".pdf", ".PDF", ".docx"],
    "Zip": [".zip", ".rar", ".7z", ".7"],
    "Krita": [".avif"],
    "Instaladores": [".msi"],
    "SQL": [".sql"],
    "Executáveis": [".exe"],
    "Json": [".json"],
    "Audio": [".mp3"],
    "Video": [".webm"],
    "PowerPoint": [".pptx"],
    "Word": [".word", ".rtf"],
    "Power BI": [".pbix", ".pbit"],
    "Save": [".save", ".rpgsave"],
    "Python": [".py"],
    "Torrent": [".torrent"],
    "C": [".c"],
    "HTML": [".html", ".htm"],
    "Java": [".java"],
    "C++": [".cpp"],
    "JavaScript": [".js"]
}

#Loop de cada arquivo dentro da pasta selecionada
for arquivo in files_list:
    #Separando o nome do arquivo e sua extensão
    nome, ext = os.path.splitext(f"{path}/{arquivo}")
    #Loop para acessar o dicionário
    for pasta in locais:
        #Procurando a Extensão do arquivo no dicionário
        if ext in locais[pasta]:
            #Verificando a existência da pasta correspondente
            if not os.path.exists(f"{path}/{pasta}"):
                #Criação do diretório correspondente
                os.mkdir(f"{path}/{pasta}")
            #Realocação do Arquivo para a pasta correspondente ao seu tipo de extensão
            os.rename(f"{path}/{arquivo}", f"{path}/{pasta}/{arquivo}")