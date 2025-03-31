from tabula import read_pdf
import pandas as pd
import zipfile
import os

# Definições dos caminhos dos arquivos
csv_path = r"teste 2\dados_procedimentos.csv"
pdf_caminho = r"C:\Users\luis felipe\workspace\teste-de-nivelamento\downloads_ans\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
zip_path = r"teste 2\Teste_LuisSilvaRezende.zip"

# Mapeamento das abreviações para descrições completas
legenda = {
    "OD": "Odontologia",
    "AMB": "Ambulatorial"
}

def extrair_tabela(pdf_caminho):

    # Lê todas as tabelas do pdf
    tabelas = read_pdf(pdf_caminho, pages="3-181", multiple_tables=True)

    df = pd.concat(tabelas, ignore_index=True)

    df.replace(legenda, inplace=True)

    return df

def salvar_como_csv(df, csv_path):
    """Salva o DataFrame como CSV"""
    df.to_csv(csv_path, index=False, header=False, encoding="utf-8")

def compactar_csv(csv_path, zip_path):
    """Compacta o arquivo CSV dentro de um ZIP"""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))

# Execução

df_tabela = extrair_tabela(pdf_caminho)
salvar_como_csv(df_tabela, csv_path)
compactar_csv(csv_path,zip_path)

print(f"Processo concluído! Arquivo ZIP gerado: {zip_path}")