
# break: permet de sortir la boucle en cours
# continue, arrête l'itération en cours et continue à la prochaine itération

for i in range(0, 100):
    if i % 2 == 0:
        print("Nombre pair", i)
    elif i == 98:
        break
    elif i % 11 == 0:
        print("Multiple de 11")
        continue
    print("fin de l'itération", i)

