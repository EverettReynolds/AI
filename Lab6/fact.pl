
fact(0,1).

fact(N,Fact) :-
	N > 0,
	fact(NMinus1,FactMinus1),
	Fact is N * FactMinus1.	
