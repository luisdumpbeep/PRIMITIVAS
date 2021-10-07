from opBaseDatos import *

def numeroCiclos(limiteCiclos):

    numerosSalidos=[]
    ciclos = 0
    contadorSorteos = 0
    sorteos = leeSorteos()


    for sorteo in sorteos:
    
        contadorSorteos = contadorSorteos + 1
        numerosSalidos = existenNumeros(sorteo, numerosSalidos)
        
        if (cambioCiclo(numerosSalidos)):
            ciclos = ciclos +1
            print(f"EL NUMERO DE SORTEOS PARA EL CICLO {ciclos} es {contadorSorteos}")
            numerosSalidos = []
            contadorSorteos = 0

        if (ciclos == limiteCiclos):
            break

    print("FIN DEL CONTEO")


def existenNumeros(numero, numerosSalidos):
    for x in range(1,7):
        if not(numero[x] in numerosSalidos):
            numerosSalidos.append(numero[x])
    return numerosSalidos
            

def cambioCiclo(numeroSalidos):
    if (len(numeroSalidos)==49):
        return True


numeroCiclos(10)
