import os
from dotenv import load_dotenv
from services.web_scraper_service import WebScraper

load_dotenv()

scraper = WebScraper()

test_id = os.getenv('TEST_NUMBER')

output = scraper.get_dashboard_information(test_id)

print(output)