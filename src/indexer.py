def indexar_por_tema(normativas):
    indice = {}

    for norma in normativas:
        tema = norma["tema"]
        indice.setdefault(tema, []).append(norma)

    return indice
