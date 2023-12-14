class Secuencia_RNA(object):
    def __init__(self):
        self.id = None
        self.compatibilidad = None
        self.secuencia = None

def ordenamientoMezcla(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = []
        for i in range(0, medio):
            izquierda.append(lista[i])
        derecha = []
        for i in range(medio, len(lista)):
            derecha.append(lista[i])
        izquierda = ordenamientoMezcla(izquierda)
        derecha = ordenamientoMezcla(derecha)
        if izquierda[medio - 1].compatibilidad <= derecha[0].compatibilidad:
            izquierda += derecha
            return izquierda
        resultado = mezcla(izquierda, derecha)
        return resultado

def mezcla(izquierda, derecha):
    lista_mezclada = []
    while len(izquierda)>0 and (len(derecha) > 0):
        if izquierda[0].compatibilidad < derecha[0].compatibilidad:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    if len(derecha) > 0:
        lista_mezclada += derecha
    return lista_mezclada

def secuencial(lista, info):
    estr = ""
    for a in lista:
        if a.id == info:
            print(a.id)
            print(a.compatibilidad)
            for b in a.secuencia:
                estr += b
            print(estr)
            estr = ""
            return True
    print("no se encontro, intente con otro valor")