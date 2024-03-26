from bs4 import BeautifulSoup
import requests

def scrapeZillowListing(url):
    # Start a session to keep cookies and headers consistent across requests
    session = requests.Session()

    # set headers to pass human test
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'Referer': 'https://www.google.com/'
    }

    response = session.get(url, headers=headers)
    try:
        if not response.status_code == 200:
              raise ValueError("Unsuccessful webscrape")
        data = {}
        # parsing
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        

        # getting address
        address = soup.find('h1')
        data['address'] = address.get_text()

        # getting images
        image = soup.find(lambda tag: tag.name == 'img' and tag.get('src').startswith('https://photos'))
        data['img'] = image.get('src')

        # getting price
        price = soup.find(lambda tag: tag.name == 'span' and tag.get_text().strip().startswith('$'))
        data['price'] = price.get_text()

        # getting bed, bath, and sqare footage
        bbs_divs = soup.findAll('div', attrs={'data-testid': 'bed-bath-sqft-fact-container'})
        for parent_div in bbs_divs:
            children = parent_div.findAll('span')
            values = []
            for child in children:
                    values.append(child.get_text())
            data[values[1]] = values[0]
        print(data)
        return data
    except Exception as e:
            raise Exception(f"Failed to webscrape {url}.")


