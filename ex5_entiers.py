"""
Initialisez deux entiers : a = 0 et b = 10.
Ecrivez une boucle:

(a) affichant et incrémentant la valeur de a tant que celle-ci reste strictement inférieure
à celle de b.

(b) décrémentant la valeur de b et affichant sa valeur si celle-ci est impair. Bouclez tant
que b n'est pas nul
"""

a, b = 0, 10

while a < b:
    print(a)
    a += 1

print("-----")

while b > 0:
    if b % 2 == 1:
        print(b)
    b -= 1
