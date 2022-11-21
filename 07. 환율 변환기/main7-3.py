import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }
    
    response = requests.get("https://kr.investing.com/currencies/{}-{}-converter".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    print(content)

    #containers = content.find('span', {'data-test': 'instrument-price-last'})
    containers = content.find('span', '#last_last')
    print(containers) 
       
get_exchange_rate('usd', 'krw')