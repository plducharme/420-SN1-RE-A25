import time

while True:
    print("L'heure actuelle est:", time.strftime("%H:%M:%S"))
    reponse = input("Voulez-vous continuer à afficher l'heure [o/n]: ")

    if reponse == "n":
        # l'instruction break permet de sortir de la boucle cours
        break

print("Fin du programme!")

