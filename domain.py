def generar_trigramas(texto):
    palabras = texto.split()
    trigramas = {}
    
    for i in range(len(palabras) - 2):
        clave = (palabras[i], palabras[i + 1])
        siguiente = palabras[i + 2]
        
        if clave in trigramas:
            trigramas[clave].append(siguiente)
        else:
            trigramas[clave] = [siguiente]
            
    return trigramas