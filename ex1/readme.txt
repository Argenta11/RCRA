Autores:
    - Alejandro García García
    - Marta Martín de Argenta Hernández

Indicaciones para la ejecución:

Para la ejecución del archivo, en primer lugar se ejecutará el siguiente comando en primer lugar:
python3 encode.py hitori1.txt hitori.lp

Los archivos usados son los siguientes:    
    - encode.py es el programa python encargado de la codificación
    - hitori1.txt se trata de un ejemplo de txt con el tablero que queremos resolver
    - hitori.lp es el archivo .lp en el que se guardará el código que utilizaremos en la decodificación

A continuación, se procederá a la decodificación mediante el siguiente comando:
clingo hitori.lp hitoriP.lp | python decode.py solution1.txt

Los archivos usados son los siguientes:
    - hitori.lp es el archivo que codificamos antes
    - hitoriP.lp es el archivo en el que tenemos declaradas los factores
    - decode.py es el programa python encargado de la decodificación
    - solution1.txt es el archivo donde saldrá el resultado del tablero que introdujimos al principio

NOTA: Para probar se utilizaron los distintos archivos proporcionados por la asignatura. 
Para ello, se cambiaría hitori1.txt por hitori2.txt, hitori3.txt, hitori4.txt, hitori5.txt y hitori6.txt
Y, consecuentemente, solution1.txt por solution2.txt, solution3.txt, solution4.txt, solution5.txt y solution6.txt