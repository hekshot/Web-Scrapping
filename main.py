import requests
import pandas as pd
import matplotlib.pyplot as plt


headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': 'defaultLang=en; nsit=vrBx3vZy122NLNOE307dk3Fl; AKA_A2=A; ak_bmsc=333F45E5502D29B2DDA6F6502E6B9C15~000000000000000000000000000000~YAAQHl3SF2wWH2OMAQAADjXS2Bb2qq1hx2aKX6Ma/tCm+U0IZRVYV6uaYiZpQ/WesXu7JaKbo7O2+S5Ymh4s59X9KRq0N+MN1++PEbBkBvWAcOJA/B/lvcPbKVm6MHY/vNnUrSvj3EagUxyNGWPYBr7F3/dk3wwlkcTszZ5676dC7BsVZx1oL14haCpd3Q5x/G92RCZNwbVlYg8PqU2V4U3S9exR9AA2lo49lM19W6q7yhEqmwRkEn7DLEVb6C2qI3+Z595p1e8Z1tXeqUX8jEP+S4jvzS/WdblCuU+EL/qjmIpfEXHpGy++aoNdoM3kAl1CiDs5zwOIsLAF8HA80ZplpV2mbIECJYYFRP/RGeEy6Ur0IOFWLpJr+OLuec918WSAFhLR/9O73m6F; nseQuoteSymbols=[{"symbol":"ADANIPORTS","identifier":null,"type":"equity"},{"symbol":"RELIANCEP1","identifier":null,"type":"equity"},{"symbol":"TATAMOTORS","identifier":null,"type":"equity"}]; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcwNDQ0NDg0NCwiZXhwIjoxNzA0NDUyMDQ0fQ.5St0RbHfnifWv3TTzIKsRlQDx0H_YR0_Pg3s54j4_tU; bm_mi=BF6A2D677481D814E0AD8F101463A670~YAAQHl3SFz4pH2OMAQAAl1rU2BY1uhlU3Pem+nTJpkwPR03xraZnaA9GVDCT+LO4XK0/41JdxdEUycmMyWh1Q2TL25lwayOAsjzq4XdyrjD5eBcjQvH4MKkIkKICnyzNE/+9K7pq6ZgQcd8fwJXw/43Pohmad5eSM6sqA63mds4WyXdqT/VgS87BocUwjaRmZImZiCNq/+a7NRV0nN5WQt4MWI2RTwY8WTAWBo/OO+2vxJLDII4wKcv7cq3catONvT9pEE2UBDBtTFjcMyUl7SYxG5Rf84F1BOHjhDwC0ObZEOuGL4/xHWF1u4aqiG5iRqU6HzTrJMSu8i9ybCvFB48=~1; bm_sv=4B213FCC22571BEAD38580802F68CE2E~YAAQHl3SF4EpH2OMAQAADl/U2BazRN4d6+12+6Jyirn2W0BEHMLeZNkHVqA+k4LYZgZdj6eSeFu4cxKsNPKamWXjrK+dw06KGspoRKkkYArzl8s0Tj5BHe3jCVs62rnOMUudawQ22MyZGtIyvU1HtPS5fJDtNT691vycWl5+fGkg32B5h4J0NnUsoq7xcspc0wtmR/nfk640I//xP+UcU61sqeyc72Ruq/QaDJEt1H6nrZoWV9MoHSmFt38h6Qw9Wiau~1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

response = requests.get(url="https://www.nseindia.com/api/chart-databyindex?index=TATAMOTORSEQN", headers=headers)

tata = pd.DataFrame(response.json()['grapthData'])
#epoch format

tata.columns = ['TimeStamp','Price']

tata['TimeStamp'] = pd.to_datetime(tata['TimeStamp'], unit='ms')

plt.plot(tata['TimeStamp'], tata['Price'])
plt.xlabel('TimeStamp')
plt.ylabel('Price')
plt.title('TATAMOTORS Stock Price')
plt.show()

print(tata.head())