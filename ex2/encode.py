#Autores:
#   - Alejandro García García
#   - Marta Martín de Argenta Hernández

import csv,sys

# Función auxiliar para agrupar las casillas de cada pieza
def buscar_pieza(array,pieza,casilla):
    for x in array:
        if x[0]==pieza:
            x.append(casilla)
            return 0
    array.append([pieza,casilla])
    return 0

# Función auxiliar para escribir en el documento las piezas según si son verticales u horizontales
def escribir_piezas(piezas,writer):
    for x in piezas:
        count=-1
        for a in x:
            count+=1
        verhor=""
        if(x[1][0]==x[2][0]):
            verhor="hor"
        else:
            verhor="ver"    
        writer.write("pieza("+x[0]+",c("+x[1][1]+","+x[1][0]+"),"+verhor+","+str(count)+").")

# Función auxiliar que obtiene el tamaño del tablero
def num_rows(file):                                                   
    with file as fp:
        return len(fp.readline())                                   

# Función auxiliar que escribe parte del objetivo dependiendo de si la pieza es vertical u horizontal
def es_vertical(lista,pieza,write,file):
    car=file.read(1)
    for x in lista:
        if x[0]==pieza:
            count=-1
            for a in x:
                count+=1
            if x[1][1]==x[2][1]:
                write.write("c("+x[1][1]+","+car+"),ver,"+str(count)+").")
            else:
                write.write("c("+car+","+x[1][0]+"),hor,"+str(count)+").")

# Función que escribe el objetivo 
def escribir_final(file,write,lista):
    file.read(1)
    pieza=file.read(1)
    write.write("#program final.\n")
    write.write("goal :- pieza("+pieza)
    write.write(",")
    file.read(1)
    es_vertical(lista,pieza,write,file)
        

if __name__ == "__main__":

   name = sys.argv[1]                                                # El primer argumento que le pasamos es el nombre del archivo
   salida = sys.argv[2]                                              # El segundo argumento que le pasamos es el archivo de salida
   file = open(name,"r")                                             # Abre el archivo en modo lectura
   
   #Inicializacion de variables
   i = 0
   j = 0
   lista = []

   reader = csv.reader(name)                                        # Lee el archivo con ese nombre
                                                        
   rows_cols = num_rows(file)-1                                     # Obtenemos el numero de filas y columnas
   
   file = open(name,"r")                                            # Abrimos el archivo en modo lectura
   write = open(salida,'w')                                         # Abrimos el archivo en modo escritura

   # Definimos las constantes 
   write.write("#program always.\n")
   write.write("#const n="+str(rows_cols)+".")
   write.write("\n")     
   write.write("distancia(-5..-1;1..5).")                                        
   write.write("\n\n")
   

   while 1:                                                         # Bucle infinito hasta que acabe el programa
       
       car = file.read(1)                                           # Leemos 1 byte del archivo (un caracter = una casilla)
                                             
       if i<=rows_cols-1:                                           # Mientras queden columnas en la fila
            write.write("cell(c("+str(j)+","+str(i)+")).")          # Escribimos en el archivo la nueva casilla
            if car!='.':
                buscar_pieza(lista,car,[str(j),str(i)]) 
            i+=1                                                    # Pasamos a la siguiente columna de la fila
       if((i == rows_cols) & (car == '\n')):                        # Si se acaban los valores de la fila actual
        i = 0                                                       # Primer valor de la fila (columna 0)
        j += 1                                                      # Fila siguiente
        write.write("\n")                                           # Salto de linea para representar en la siguiente fila
       if ((i == rows_cols) & (j == rows_cols-1)):                  # Si acabamos las filas del tablero
        # Escribimos las restricciones
        write.write("\n\n")
        write.write("#program initial.\n")
        escribir_piezas(lista,write)
        write.write("\n")
        write.write("\n")
        escribir_final(file,write,lista)
        break                                                               # Acaba el programa 
 