import requests

url = "https://api.exchangeratesapi.io/v1/latest?access_key=466ea74ce6de1e0436ae7e9410eca725&base=USD&symbols=EUR,RUB"

response = requests.request("GET", url)

print(response.content)