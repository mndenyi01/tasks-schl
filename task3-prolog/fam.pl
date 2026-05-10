% --- Genders ---
male(albert). male(bob). male(charlie). male(david). male(edward).
female(alice). female(barbara). female(claire). female(diana). female(eliza).

% --- Family Relationships (parent(Parent, Child)) ---
% Grandparents to Parents
% Albert and Alice are Bob and Diana's parents; and they are also Charlie, Claire, Edward, and Eliza's grandparents.
parent(albert, bob).
parent(alice, bob).
parent(albert, diana).
parent(alice, diana).

% Parents to Children
% Bob and Barbara are Charlie and Claire's parents.
parent(bob, charlie).
parent(barbara, charlie).
parent(bob, claire).
parent(barbara, claire).

% Parents to Grandchildren (The "Other" Side)
% Diana and David are Edward and Eliza's parents.
parent(diana, edward).
parent(david, edward).
parent(diana, eliza).
parent(david, eliza).

% Relationship Rules for the family tree.
% Basic Parent Types
father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).

% Grandparent rules
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% Sibling rules
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y. % Siblings share at least one parent and are not the same person.

% Uncles and Aunts (Sibling of a parent)
uncle(U, N) :- male(U), sibling(U, P), parent(P, N).
aunt(A, N) :- female(A), sibling(A, P), parent(P, N).

% Cousins (Children of siblings)
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).