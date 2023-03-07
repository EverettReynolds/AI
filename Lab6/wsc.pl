

is_in_class(toby,csc380).
is_in_class(bob,csc480).
is_in_class(toby,csc480).
is_in_class(everett,csc340).
is_in_class(everett,phy141).


is_in_room(csc480,wsc100).
is_in_room(csc380,wsc238).
is_in_room(csc340,wsc238).
is_in_room(phy141,seb114).


has_temperature(wsc100,65).
has_temperature(wsc238,92).
has_temperature(seb114,72).




/*is_hot(Person) :-
        is_in_class(Person,Class),
        is_in_room(Class,Room),
        has_temperature(Room,Temp),
        Temp > 80.*/


is_hot(Person) :-
        is_in_class(Person,_),
        is_in_room(_,_),
        has_temperature(_,Temp),
        Temp > 80.




