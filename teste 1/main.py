import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import zipfile

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Pasta onde os PDFs serão salvos
PASTA_DOWNLOADS = "downloads_ans"
os.makedirs(PASTA_DOWNLOADS, exist_ok=True)

def baixar_pdf(nome_arquivo, url):
    """Baixa um arquivo PDF e salva localmente."""
    resposta = requests.get(url, stream=True)
    if resposta.status_code == 200:
        caminho_arquivo = os.path.join(PASTA_DOWNLOADS, nome_arquivo)
        with open(caminho_arquivo, "wb") as f:
            for chunk in tqdm(resposta.iter_content(chunk_size=1024), desc=f"Baixando {nome_arquivo}", unit="KB"):
                f.write(chunk)
        return caminho_arquivo
    return None

requisicao = requests.get(URL)
soup = BeautifulSoup(requisicao.text, "html.parser")

links = soup.find_all("a", href=True) # Pegar todos os links da página

# Filtrar os PDFs que correspondem a "Anexo I" e "Anexo II"
pdfs_para_baixar = {}
for link in links:
    href = link["href"]
    if ("Anexo_I" in href or "Anexo_II" in href) and href.endswith(".pdf"):  # Ajuste se necessário
        nome_arquivo = href.split("/")[-1]
        pdfs_para_baixar[nome_arquivo] = href


# Baixar os PDFs encontrados
arquivos_baixados = []
for nome, url in pdfs_para_baixar.items():
    caminho = baixar_pdf(nome, url)
    if caminho:
        arquivos_baixados.append(caminho)

# Criar um ZIP com os anexos baixados
if arquivos_baixados:
    zip_filename = "Anexos_ANS.zip"
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for arquivo in arquivos_baixados:
            zipf.write(arquivo, os.path.basename(arquivo))
    print(f"\nArquivo ZIP criado: {zip_filename}")
else:
    print("\nNenhum anexo foi baixado.")