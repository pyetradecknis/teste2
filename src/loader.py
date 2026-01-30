import json
from pathlib import Path

def carregar_normativas(caminho: str):
    arquivo = Path(caminho)

    if not arquivo.exists():
        raise FileNotFoundError("Arquivo de normativas não encontrado.")

    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)
