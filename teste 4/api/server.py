from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite requisições de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Carregar os dados do CSV
CSV_PATH = r"C:\Users\luis felipe\workspace\teste-de-nivelamento\teste 3\Relatorio_cadop.csv"
df = pd.read_csv(CSV_PATH, delimiter=";", encoding="utf-8")
df = df.fillna("")  # Substitui NaN por string vazia

# Rota para buscar operadoras
@app.get("/buscar/")
def buscar_operadoras(query: str = Query(..., min_length=3)):
    resultados = df[df["Nome_Fantasia"].str.contains(query, case=False, na=False)].to_dict(orient="records")
    return {"resultados": resultados[:10]}  # Retorna os 10 primeiros resultados

# Rodar o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)