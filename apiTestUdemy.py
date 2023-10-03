import requests

url = "https://pokeapi.co//api/v2/pokemon/1"
url2 = "https://pokeapi.co//api/v2/pokemon/2"
payload = ""
headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
response2 = requests.request("GET", url2, headers=headers, data=payload)
# print(response.text)
print(response2)
print(response2.text)