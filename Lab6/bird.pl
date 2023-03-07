hascovering(bird,feathers).
hasproperty(bird,flies).
hascolor(bluebird,blue).
hassize(bluebird,small).
isa(bluebird,bird).
isa(bird,vertebrate).

is_bird(Animal) :-
	hascovering(Animal,feathers),
	hasproperty(Animal,flies),
	hassize(Animal,_),
	hascolor(Animal,_),
	Animal == bird.

