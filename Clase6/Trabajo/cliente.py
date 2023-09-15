import requests

url = 'https://ominous-space-fishstick-pjrp9j9rx9vgf9pp4-8000.app.github.dev/'

r = requests.get(url)
print(r.text)

r = requests.post(url + 'encolar', json={'nombre': 'juan', 'productos': ['manzana', 'pera'], "Documento": 12345})
r = requests.post(url + 'encolar', json={'nombre': 'joseph', 'productos': ['manzana', 'manzana'], "Documento": 12345})
r = requests.post(url + 'encolar', json={'nombre': 'pedro', 'productos': ['manzana', 'pera'], "Documento": 12345})
r = requests.post(url + 'encolar', json={'nombre': 'pablo', 'productos': ['manzana', 'mango'], "Documento": 12345})
print(r.text)

