from os import linesep, supports_bytes_environ
import sqlite3
from sqlite3.dbapi2 import connect
import opBaseDatos

def leeEstadisticas(campo):

    conexion = sqlite3.connect("PRIMITIVA.db")
    cursor = conexion.cursor()
    comando = f"SELECT {campo} FROM tablaEstadisticas ORDER BY sorteo DESC"
    cursor.execute(comando)
    tResultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return tResultados


def fMediaSumas():
    print("NUM LIMITADOR DE SORTEOS: ")
    limitador = int(input())

    opBaseDatos.borrarDatostablaSorteo()
    
    for suma in range(21,280):
        lista = extraeAgrupacionSuma(suma, limitador) 
        ultimaVez = lista[0]
        contador = len(lista)-1
        listaOrdenada = sorted(lista)
        mediaNormal = haceMedia(lista)
        lista = acotarLista(listaOrdenada)
        mediaRecortada = haceMedia(lista)
        opBaseDatos.insertarDatosSumas (suma, contador, mediaNormal, mediaRecortada, ultimaVez)
    print("FIN DEL PROCESO")         

def extraeAgrupacionSuma (suma, numLimitador):
    contador = 0
    lAparaciones = []

    print(suma)

    tResultados = leeEstadisticas("suma")
    tResultados = limitaSorteos(tResultados, numLimitador)
    for sorteo in tResultados:

        contador = contador + 1 

        if (suma == sorteo[0]):
            lAparaciones.append(contador)
            contador = 0
    lAparaciones.append(contador)
    return lAparaciones

def acotarLista(lista):
    elementos = int(len(lista)*0.25)
    if (elementos > 0):
        for x in range(0,elementos):
            lista.pop(0)
            lista.pop()
    return lista

def haceMedia(lista):
    media = 0
    for numero in lista:
        media = media + numero
    media = int(media/len(lista))
    return media

def limitaSorteos(ltSorteos, numLimite):
    while (len(ltSorteos) > numLimite):
        ltSorteos.pop()
    return ltSorteos

fMediaSumas()
