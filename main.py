
# Import libraries
import json
import requests
import matplotlib.pyplot as plt

  
# Defining Binance API URL
url = "https://data.binance.com/api/v3/ticker/24hr" 
data = requests.get(url)
data = data.json()


symbols = [item.get('symbol') for item in data]
symbol=[]
for i in range(0,20): 
    symbol.append(symbols[i])
price= [item.get("askPrice") for item in data]
prices=[]
for i in range(0,20): 
    prices.append(price[i])

print(symbol)
graphs=plt.bar(symbol,prices)
colors=['r','g','b']
for i in range(0,20): 
    graphs[i].set_color(colors[i%3])
plt.title("PRICES")
plt.show()






