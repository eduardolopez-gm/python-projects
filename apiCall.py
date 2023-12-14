import requests
# Set endpoint url
url = "https://api.coincap.io/v2/markets"
# Get endpoint response 
response = requests.get(url)
# ForEach element in response.data print its value 
for index,element in enumerate(response.json()["data"]):
    print(f"Index: {index}, Value: {element} \n")
