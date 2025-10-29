# open(nom, mode) permet d'ouvrir un fichier soit en lecture, en écriture ou les deux
# modes: r = lecture, w = écriture, a = append, x = exclusif, b = binaire, t = texte (par défaut)
liste_fibo = []
with open("fibo.txt", mode="r") as fichier:
    for ligne in fichier:
        # strip enlève le caractère spécifié en début et fin de str
        liste_fibo.append(ligne.strip("\n"))

print(liste_fibo)
