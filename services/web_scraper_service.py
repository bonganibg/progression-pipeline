import os 
import requests
from bs4 import BeautifulSoup


class WebScraper():
    BASE_URL = os.getenv('BASE_URL')

    def get_dashboard_information(self, number: str):
        url = self.BASE_URL + number

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html5lib')
        
        table = soup.find('table', attrs={'class': 'table'})

        table_body = table.find('tbody')

        output = []

        for row in table_body.find_all('tr'):
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            output.append(cols)

        return output