import flask

app = flask.Flask("fruits")

def get_page(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/")
def homepage():
    return get_page("index")

@app.route("/about")
def homepage():
    return get_page("about")