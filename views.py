from app import app, cur 

@app.route('/')
def hello_view(self):
    cur.execute("SELECT page_title FROM page WHERE page_title LIKE '%Republic%'")
    data = cur.fetchall()
    return "SELECT page_title FROM page WHERE page_title LIKE '%Republic%'\n{}".format(data)

