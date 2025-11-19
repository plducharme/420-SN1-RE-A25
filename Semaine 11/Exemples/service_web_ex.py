import requests

# Exemple d'appel à un service web
# https://pokeapi.co/api/v2/pokemon/{id du pokemon}/
numero_du_pokemon = input("Entrez le numéro du pokémon: ")
dictionnaire_reponse = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero_du_pokemon}/").json()

print(f"Nom: {dictionnaire_reponse["name"]}")

for habilete in dictionnaire_reponse["abilities"]:
    print(habilete["ability"]["name"])
