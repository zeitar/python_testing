import requests

status = 'available'

res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.text)
print(res.json)
print(type(res.json()))