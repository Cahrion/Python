import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)

for a in result:
    print(f"Numarası: {a['userId']} adı: {a['id']}")
