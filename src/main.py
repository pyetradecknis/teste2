from loader import carregar_normativas
from indexer import indexar_por_tema
from search import buscar_por_palavra

def main():
    normativas = carregar_normativas("../data/normativas.json")

    indice_temas = indexar_por_tema(normativas)

    print("Temas disponíveis:")
    for tema in indice_temas:
        print("-", tema)

    termo = input("\nBuscar por palavra-chave: ")
    resultados = buscar_por_palavra(normativas, termo)

    print(f"\nResultados encontrados ({len(resultados)}):")
    for r in resultados:
        print(f"{r['numero']} ({r['status']}) - {r['tema']}")

if __name__ == "__main__":
    main()
