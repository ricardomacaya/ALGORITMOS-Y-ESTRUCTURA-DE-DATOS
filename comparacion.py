from datos import seqs, seqr
from classs import *

class bcolors:
    OK = "\033[92m"  # GREEN
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR

def crear():
    lista= []
    for a in range(len(seqs)):
        seq = Secuencia_RNA()
        seq.id = a+1
        seq.compatibilidad = 0
        seq.secuencia = seqs[a]
        lista.append(seq)
    return lista

def comparacion(lista,seqr):
    print("\n")
    for b in lista:
        if b.compatibilidad != 0:
            pass
        else:
            for a in range(150):
                if b.secuencia[a] == seqr[a]:
                    b.compatibilidad += 1
                    b.secuencia[a] = bcolors.OK + b.secuencia[a] + bcolors.RESET
                else:    
                    b.secuencia[a] = bcolors.FAIL + b.secuencia[a] + bcolors.RESET
            b.compatibilidad = (b.compatibilidad/150)*100

def imprimir(lista):
    estr = ""
    for a in lista:
        print("[",a.id,"]")
        print("[",a.compatibilidad,"%","]")
        for b in a.secuencia:
            estr += b
        print("[",estr,"]")
        estr = ""

def imprimir_porcentaje(lista):
    c = 0
    list_p = []
    for a in lista:
        for b in list_p:
            if b == None:
                list_p.append([a.compatibilidad,1])
                c = 1
            if a.compatibilidad == b[0]:
                b[1] += 1
                c = 1
        if c == 0:
            list_p.append([a.compatibilidad,1])
        c = 0        
    return list_p

def eliminar(lista, info):
    for a in lista:
        if a.id == info:
            lista.remove(a)

def insertar(lista):
    new = Secuencia_RNA()
    new.compatibilidad = 0
    pase = 0
    while True:
        ide = int(input("Ingrese el valor id: "))
        for a in lista:
            if a.id == ide:
                print("Este id ya existe, porfavor ingrese otro")
                pase = 1
        if pase == 0:
            new.id = ide
            seq = []
            for a in range(len(lista[0].secuencia)):
                while True:
                    print(a)
                    nuc = str(input("Ingrese un nucleotido: "))
                    if nuc.upper() == "A" or nuc.upper() == "U" or nuc.upper() == "C" or nuc.upper() == "G":
                        seq.append(nuc.upper())
                        print(seq)
                        break
                    else:
                        print("Ese nucleotiodo no existe o no es compatible, ingrese otro")
            if len(seq) == 150:
                new.secuencia = seq
                lista.append(new)
                print(new.id)
                print(new.compatibilidad)
                print(new.secuencia)
                return lista
            else:
                "Algo salio mal, no se pudo agregar su muestra"
                break

def clear():
    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
             \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
             \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n""")

def main():
    estr = ""
    clear()
    lista = crear()
    print("Analisis Realizado")
    comparacion(lista,seqr)
    lista = ordenamientoMezcla(lista)
    lp = imprimir_porcentaje(lista)
    while True:
        opcion = str(input("""
(0)Salir
(1)Buscar la secuencia con mayor relacion
(2)Buscar la secuencia con menor relacion
(3)Buscar por (ID)
(4)Mostrar cantidad por porcentaje
(5)eliminar dato
(6)Insertar muestra
(7)Volver a comparar
ingrese un numero: """))
        if opcion == int:
            opcion = int(opcion)
        elif opcion == "0":
            break
        elif opcion == "2":
            clear()
            print((lista[0]).id)
            print((lista[0]).compatibilidad)
            for a in (lista[0]).secuencia:
                estr += a 
            print(estr)
            estr = ""
        elif opcion == "1":
            clear()
            print((lista[len(lista)-1]).id)
            print((lista[len(lista)-1]).compatibilidad)
            for a in (lista[len(lista)-1]).secuencia:
                estr += a 
            print(estr)
            estr = ""
        elif opcion == "3":
            clear()
            ide = int(input("ingrese el id a buscar: "))
            clear()
            secuencial(lista,ide)
        elif opcion == "4":
            clear()
            for a in lp:
                print("[",a[0],"%","=",a[1],"]")
        elif opcion == "5":
            clear()
            info = int(input("ingrese el id del dato que desea eliminar: "))
            eliminar(lista,info)
        elif opcion == "6":
            lista = insertar(lista)
        elif opcion == "7":
            comparacion(lista,seqr)

if __name__=='__main__':
    main()