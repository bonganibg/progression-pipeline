import os
import requests 
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

BASE_URL = os.getenv('URL')
URL = BASE_URL + '/' + os.getenv('TEST_NUMBER')

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.find('table', attrs={'class': 'table'})

table_body = table.find('tbody')

for row in table_body.find_all('tr'):
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)
