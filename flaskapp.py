# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

def display_html(rows):
    """
    Converts query result rows into a simple HTML table string.
    Flask routes can return this directly as a response.
    """
    html = "<table border='1'>"
    for row in rows:
        html += "<tr>"
        for col in row:
            html += f"<td>{col}</td>"
        html += "</tr>"
    html += "</table>"
    return html

@app.route('/')
def top_countries():
    countries = get_list_of_top10python()
    return render_template('index.html', results=countries)



# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
