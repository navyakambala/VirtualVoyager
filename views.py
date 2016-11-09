from __init__ import app, cur 
from flask import render_template

#lonely planet imports
from bs4 import BeautifulSoup
import urllib2

@app.route('/')
def welcome():
    return render_template('index.html') 


@app.route('/example_query')
def example_query():
    cur.execute("SELECT page_title FROM page WHERE page_title LIKE '%Republic%'")
    query_name = "SELECT page_title FROM page WHERE page_title LIKE '%Republic%'" 
    query =  str(cur.fetchall())
    return render_template('example_query.html', query_name=query_name, query=query) 


@app.route('/virtualvoyager/trips/<keyword>', methods=['GET'])
def get_trip(keyword):
    return "hello"


def get_best_location(keyword):
    '''
    Make requests to LostVoyager API with the user inputted keyword
    Choose most popular location from request
    Return information needed to make trip and location AND IMAGE URL
    '''


    keyword = urllib2.quote(keyword)
    url = "http://www.lonelyplanet.com/search?q="+keyword+"&type=place"

    #website prevents bot scraping. pretend to be mozilla
    request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": url,
        "Connection": "keep-alive"
    }

    request = urllib2.Request(url, headers = request_headers)
    webpage = urllib2.urlopen(request).read()
    soup=BeautifulSoup(webpage, "lxml")
    #print soup.prettify().encode('UTF-8')

    content = soup.find_all("a", class_="link--wrapper")
    topResult = content[0]
    destination = ' '.join(topResult.getText().strip().split()[1:])
    smallImage = topResult.find('img')['src']
    image = smallImage[smallImage.index('http'):]

    return destination, image


def process_wiki_text(text):
    '''
    Extract pictures, coordinates, description, eat, see, do, and go next from wiki text
    '''
    return 'hello'


def create_location(attribute_dict):
    '''
    Create location from processed wiki text
    '''
    return 'hello'


def create_trip(keyword, location):
    '''
    Create trip from locations go next 
    '''
    return 'hello'

