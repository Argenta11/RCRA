#Autores:
#   - Alejandro García García
#   - Marta Martín de Argenta Hernández

import csv,sys

def num_rows(file):                                                   # Numero de filas en el archivo
    with file as fp:
        return len(fp.readline())                                     # Devuelve la longitud del numero de lineas


if __name__ == "__main__":

   name = sys.argv[1]                                                # El primer argumento que le pasamos es el nombre del archivo
   salida = sys.argv[2]                                              # El segundo argumento que le pasamos es el archivo de salida
   file = open(name,"r")                                             # Abre el archivo en modo lectura
   
   #Inicializacion de variables
   i = 0
   j = 0

   reader = csv.reader(name)                                        # Lee el archivo con ese nombre
                                                        
   rows_cols = num_rows(file)                                       # Obtenemos el numero de filas y columnas
   
   file = open(name,"r")                                            # Abrimos el archivo en modo lectura
   write = open(salida,'w')                                         # Abrimos el archivo en modo escritura


   write.write("row(0.."+str(rows_cols-2)+").")                     # Escribimos la definicion de las filas, de 0 a rows-1 (numero igual a filas)
   write.write("\n")                                 
   write.write("col(0.."+str(rows_cols-2)+").")                     # Escribimos la definicion de las columnas, 0 a cols-1 (numero igual a columnas)
   write.write("\n")     
   write.write("val(0..9).")                                        # Escribimos que los numeros pueden ir de 0 a 9
   write.write("\n\n")

   while 1:                                                         # Bucle infinito hasta que acabe el programa
       num = file.read(1)                                           # Leemos 1 byte del archivo (un caracter = una casilla)
                                             
       if i<=rows_cols-2:                                           # Mientras queden columnas en la fila
        write.write("cell(c("+str(j)+","+str(i)+","+str(num)+")).") # Escribimos en el archivo la nueva casilla (Escribimos en la celda (j,i) el valor num)

        i+=1                                                        # Pasamos a la siguiente columna de la fila
       if((i == rows_cols-1) & (num == '\n')):                      # Si se acaban los valores de la fila actual
        i = 0                                                       # Primer valor de la fila (columna 0)
        j += 1                                                      # Fila siguiente
        write.write("\n")                                           # Salto de linea para representar en la siguiente fila
       if ((i == rows_cols-1) & (j == rows_cols-2)):                # Si acabamos las filas del tablero
        break                                                       # Acaba el programa
   

  
 
