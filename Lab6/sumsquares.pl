
square(1,1).

square(N,Nsum) :-
	N > 1,
	NMinus1 is N-1,
	N2 is N*N,
	square(NMinus1,Sum),
	Nsum is N2 + Sum.


