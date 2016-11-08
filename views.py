from __init__ import app, cur 
from flask import render_template


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
    Return information needed to make trip and location
    '''
    return 'hello'


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

