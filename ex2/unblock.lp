% Alejandro García García
% Marta Martín de Argenta Hernández

#program always.

% Definimos casillas ocupadas por una pieza
ocupado(V,c(X,C)) :- pieza(V,c(X,Y),ver,L), cell(c(X,C)), C>=Y, C<=(Y+L-1).
ocupado(V,c(B,Y)) :- pieza(V,c(X,Y),hor,L), cell(c(B,Y)), B>=X, B<=(X+L-1).

#program dynamic.

% Effect axions: definimos moverse

pieza(A,c(X,Y+N),ver,L) :- 'pieza(A,c(X,Y),ver,L), move(A,N).
pieza(A,c(X+N,Y),hor,L) :- 'pieza(A,c(X,Y),hor,L), move(A,N).

% Executability constraints

:- 'pieza(A,c(X,Y),ver,L), move(A,N), Y+N<0.
:- 'pieza(A,c(X,Y),ver,L), move(A,N), Y+N+L>n.

:- 'pieza(A,c(X,Y),hor,L), move(A,N), X+N<0.
:- 'pieza(A,c(X,Y),hor,L), move(A,N), X+N+L>n.


:- 'pieza(A,c(X,Y),ver,L), 'ocupado(B,c(X,W)), A!=B, move(A,N), N>0,Y+L+N>W, Y+L<=W.
:- 'pieza(A,c(X,Y),ver,L), 'ocupado(B,c(X,W)), A!=B, move(A,N), N<0,Y+N<=W, Y>W.

:- 'pieza(A,c(X,Y),hor,L), 'ocupado(B,c(W,Y)), A!=B, move(A,N), N>0,X+L+N>W, X+L<=W.
:- 'pieza(A,c(X,Y),hor,L), 'ocupado(B,c(W,Y)), A!=B, move(A,N), N<0,X+N<=W, X>W.

% Inertia: c(F) = fluent F has changed
pieza(V,X,C,L) :- 'pieza(V,X,C,L), not move(V,_).


% generar movimientos
1 {move(A,N): 'pieza(A,_,_,_), _distancia(N)} 1.

#program final.
:- not goal.


#show move/2.
