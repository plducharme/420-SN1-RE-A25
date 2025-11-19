import json
# Un document json ressemble à un dictionnaire python
json_doc = '''
{
    "propriete1" : "valeur",
    "propriete2" : "valeur2"
}

'''
# Le built-in json permet de transformer une str json en dictionnaire python et l'inverse
dictionnaire = json.loads(json_doc)
print(dictionnaire)

print(json.dumps(dictionnaire))
