# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *
from flask import session
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UserCodeLangs')


app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Extract form data
        username = request.form.get('username')
        name = request.form.get('name')

        # Process the data (e.g., add it to a database)
        add_user_to_database(username, name)


        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')


@app.route('/delete-user',methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        # Extract form data
        username = request.form.get('username')

        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        delete_user_from_database(username)

        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_user.html')


@app.route('/update-user')
def update_user():
    if request.method == 'POST':
        username = request.form['username']
        lang = request.form['lang']

        update_fav_lang(username, lang)

        return redirect(url_for('home'))
    else:
        return render_template('update_user.html')


@app.route('/display-users')
def display_users():
    # Use DynamoDB to display users
    response = table.scan()
    users_list = response.get('Items', [])
    return render_template('display_users.html', users = users_list)


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




# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
