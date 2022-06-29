Autores:
    - Alejandro García García
    - Marta Martín de Argenta Hernández

Intrucciones de uso:

En primer lugar, se codifica a .lp con el encode.py mediante el siguiente comando:

python3 encode.py levelX.txt levelX.lp

    * Siendo X en ambos casos el número de nivel


En segundo lugar, se ejecutan los .lp mediante el siguiente comando:

telingo --verbose=0 --warn none unblock.lp levelX.lp > solX.txt

    * Siendo X en ambos casos el número de nivel


Finalmente, si se desea ver de forma gráfica se ejecutará el siguiente comando:

python3 showunblock.py levelX.txt solX.txt

    * Siendo X en ambos casos el número de nivel

