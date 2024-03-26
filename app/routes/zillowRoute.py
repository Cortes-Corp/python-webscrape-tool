from flask import Blueprint, request, jsonify

from ..scripts.zillowScraper import scrapeZillowListing

zillow_blueprint = Blueprint('zillow_blueprint', '__name__')

@zillow_blueprint.route('/scrape-zillow')
def scrape_zillow():
    url = request.args.get('url', 'invalid')
    if url == 'invalid':
        res = jsonify({'error': 'Invalid params' })
        res.status_code = 400
        return res
    else:
        try:
            data = scrapeZillowListing(url)
            return jsonify(data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    