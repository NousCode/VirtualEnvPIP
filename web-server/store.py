import requests

def ger_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # Para saber el estatus de la respuesta
    print(r.status_code)
    # Para saber la respuesta
    print(r.text)
    print(type(r.text))
    # Transforma de un tipo JSON a un tipo de dato de Python
    categories = r.json()
    for category in categories:
        print(category['name'])