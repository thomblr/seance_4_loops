"""
Dans le cadre d'une soirée 'bretonne' organisée par votre Cercle, on vous
demande d'écrire un parolier de chansons traditionnelles
La suite d'instruction :

n=10
print("Dans %d ans je m'en irai, j'entends le loup et le renard chanter" % i)

permet d'afficher le message "Dans 10 ans je m'en irai, j'entends le loup et le renard chanter"
Ecrivez une boucle while qui permet d'afficher :
Dans 10 ans je m'en irai, j'entends le loup et le renard chanter
Dans 9 ans je m'en irai, j'entends le loup et le renard chanter
Dans 8 ans je m'en irai, j'entends le loup et le renard chanter
...
Dans 1 an je m'en irai, j'entends le loup et le renard chanter
"""

n = 10
for i in range(n, 0, -1):
    if i <= 1:
        plur = ''
    else:
        plur = 's'

    print("Dans %d an%s je m'en irai, j'entends le loup et le renard chanter" % (i, plur))
