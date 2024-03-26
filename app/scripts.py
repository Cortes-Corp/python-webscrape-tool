from bs4 import BeautifulSoup
import requests

from time import sleep

# Start a session to keep cookies and headers consistent across requests
session = requests.Session()

# Set a custom User-Agent and Referer header
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Referer': 'https://www.google.com/'
}

url = 'https://www.zillow.com/homedetails/439-Bergen-Blvd-Oradell-NJ-07649/37986497_zpid/'

response = session.get(url, headers=headers)

if response.status_code == 200:
     # Process your successful response here
    html = response.text
    print(html)  # Or proceed with BeautifulSoup to parse the HTML
else:
        print(f'Failed to retrieve the page: status code {response.status_code}')
