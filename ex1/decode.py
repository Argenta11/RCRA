#Autores:
#   - Alejandro García García
#   - Marta Martín de Argenta Hernández

import sys
import re
import numpy as np

# Funciones auxiliares

def num_rows(file):                                                     # Numero de filas en el archivo
    with file as fp:
        return len(fp.readline())                                       # Devuelve la longitud del numero de lineas



def preparar_matriz(name,texto):                                        # Función que devuelve la matriz a partir del texto
    datos = obtener_valores(texto)                                      # Llamamos a una función auxiliar que nos devuelve la matriz de casillas
    return datos_a_matriz(datos,name)                                   # Devolvemos el resultado de la función auxiliar que nos devuelve la matriz solución

def datos_a_matriz(datos,name):                                         # Función auxiliar que nos devuelve la matriz solución
    tamaño_datos = np.shape(datos)                                      # Obtenemos las dimensiones de la matriz de los datos
    rows=int(datos[int(tamaño_datos[0])-1][0])+1                        # El número de filas de la matriz será la fila del último dato
    cols=int(datos[rows][1])+1                                          # El número de columnas de la matriz será la columna del último dato
    
    matriz = []                                                         # Inicializamos la matriz que vamos a devolver

    for var in range(rows):                                             # Recorremos todas las filas
        matriz_aux=[]                                                   # Creamos una matriz auxiliar para almacenar los datos de la fila
        for var2 in range(cols):                                        # Recorremos las columnas de la fila
            matriz_aux.append("")                                       # Como estamos inicializando la matriz, los valores son el string ""
        matriz.append(matriz_aux)                                       # Añadimos la fila completa a la matriz
    i=0
    
    for i in  range(int(tamaño_datos[0])):                              # Recorremos toda la matriz de datos
        matriz[int(datos[i][0])][int(datos[i][1])]=datos[i][2]          # Guardamos cada dato en su casilla correspondiente
    return matriz                                                       # Devolvemos la matriz con el tablero

def valor_o_negra(casilla):                                             # Función que asigna el valor a la casilla dependiendo de si es blanca o negra
    valores=re.split(r'[(,]', casilla)                                  # Eliminamos los paréntesis sobrantes y dividimos por valores de la casilla (F,C,V)
    devolver=[valores[2],valores[3], valores[4]]                        # La matriz la inicializamos con los valores (F,C,V)
    if(valores[0]=="black"):                                            # Cuando se trata de una casilla negra
        devolver[2]= "*"                                                # El valor pasa a ser un *
    return devolver                                                     # Devolvemos la casilla

def obtener_valores(texto):                                             # Función que nos devuelve una matriz con los valores de las casillas
    #Inicialización de variables
    i=0 
    a=1
    matriz=[]

    dividido= texto.split(" ")                                          # Dividimos por espacios para separar las casillas
    dividido_unido=dividido[0]                                          # Inicializamos donde vamos a almacenar todas las casillas con la primera
   
    #Nota: Lo hacemos de esta forma para poder volver a dividir después por los paréntesis que faltan y que así nos queden todas las casillas en el mismo vector
    
    for a in range(np.size(dividido)):                                  # Para el resto de casillas
        dividido_unido=dividido_unido+dividido[a]                       # Añadimos la casilla al conjunto
    dividido2 = dividido_unido.split("))")                              # Separamos las casillas por paréntesis, quedando en esta matriz
    
    tamaño = np.size(dividido2)                                         # Obtenemos el número de casillas
    for i in range(tamaño-1):                                           # Realizamos el proceso para cada casilla
        matriz.append(valor_o_negra(dividido2[i]))                      # Enviamos la casilla a la función auxiliar que decide su valor dependiendo de si es blanca o negra
    return matriz                                                       # Devolvemos la matriz con datos

def archivo_escrito(texto, salida):                                     # Función que escribe en el archivo
    #Inicialización de variables
    i=0
    j=0

    write = open(salida,'w')                                            # Abrimos el archivo en modo escritura
    tamaño_datos = np.shape(texto)                                      # Obtenemos el tamaño de los datos
    
    for i in range(tamaño_datos[0]):                                    # Para cada fila
        for j in range(tamaño_datos[1]):                                # En cada columna
            write.write(texto[i][j])                                    # Almacenamos su valor
        write.write("\n")                                               # Cuando acabamos la fila pasamos a la siguiente
    


# Main
if __name__ == "__main__":                                              # El main del programa
    lineas=sys.stdin.read()                                             # Leemos las líneas que salió de clingo
    write = open(sys.argv[1],'w')                                       # Abrimos el archivo en modo escritura
    #Inicializacion de variables
    name = sys.argv[1]                                                  # El primer argumento que le pasamos es el nombre del archivo
    lineas_divididas = lineas.split("\n")                               # Dividimos lo recogido en pantalla por líneas
    if lineas_divididas[3] == "UNSATISFIABLE":                          # Si nos dio un resultado UNSATISFIABLE
        write = open(name,'w')                                          # Abrimos el archivo en modo escritura
        write.write("El problema propuesto no tiene solucion")          # Indicamos que el problema no tiene solución
    else:                                                               # Si el problema tiene solución
        entrada = lineas_divididas[4]                                   # Cogemos la línea 4 (donde salen las casillas)
        archivo_leido = preparar_matriz(name,entrada)                   # Leemos desde el archivo hitori.lp
        archivo_escrito(archivo_leido,name)                             # Escribimos en el txt
    
 
