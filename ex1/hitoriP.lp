%Autores:
%   - Alejandro García García
%   - Marta Martín de Argenta Hernández

% Definimos las celdas que son vecinas
neighbour(c(R,C,V),c(R,C+1,V')):- cell(c(R,C,V)),cell(c(R,C+1,V')).
neighbour(c(R,C,V),c(R+1,C,V')):- cell(c(R,C,V)),cell(c(R+1,C,V')).
neighbour(X,Y):- neighbour(Y,X).


%Cada celda solo puede ser blanca o negra.
white(X):- not black(X), cell(X).
black(X):- not white(X), cell(X).

%Definimos las reglas para celdas conectadas 
connected(X,Y):- white(X), white(Y), neighbour(X,Y).


%Aplicamos transitividad para las conexiones
connected(X,Z):- white(X), white(Y), white(Z), neighbour(Y,Z), connected(X,Y), X!=Z.

%Tiene que poderse recorrer camino entre blancas
:-white(X), white(Y), not connected(X,Y), X!=Y.


% Restricciones para blancas
:- white(c(R,C,V)), white(c(R,C',V)), C!=C'.  %si estan en misma fila dos blancas, tienen que tener diferente contenido
:- white(c(R,C,V)), white(c(R',C,V)), R!=R'.  %si estan en misma columna dos blancas, tienen que tener diferente contenido



% Restricciones para negras
:- black(X), black(Y), neighbour(X,Y), X!=Y. % no adyacentes

#show white/1.
#show black/1.
