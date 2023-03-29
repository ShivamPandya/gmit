import requests

def type(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    content = requests.get(url.format(pokemon))
    content = content.json()
    poketype = content["types"][0]["type"]["name"]
    return poketype