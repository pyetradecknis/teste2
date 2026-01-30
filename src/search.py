def buscar_por_palavra(normativas, palavra_chave):
    palavra_chave = palavra_chave.lower()

    return [
        n for n in normativas
        if palavra_chave in n["descricao"].lower()
        or palavra_chave in n["tema"].lower()
    ]
