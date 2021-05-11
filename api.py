import requests


def rate_getter():
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=14ac6512ce2db0e6355ee053f6ad8827&base=EUR&symbols=USD,AMD,RUB"
    response = requests.request("GET", url)
    rates = response.json()["rates"]
    rates["EUR"] = 1
    return rates
