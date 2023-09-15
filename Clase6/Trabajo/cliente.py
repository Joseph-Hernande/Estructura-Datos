import requests

url = 'https://ominous-space-fishstick-pjrp9j9rx9vgf9pp4-8000.app.github.dev/'

r = requests.get(url)
print(r.text)

r = requests.post(url + 'encolar', json={'nombre': 'juan', 'productos': ['manzana', 'pera']})
print()

