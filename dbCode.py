# dbCode.py
# Author: Your Name
# Helper functions for database connection and queries

import pymysql
import creds
import boto3
from flask import flash

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UserCodeLangs')



def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    conn = pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
    )
    return conn

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    cur = get_conn().cursor(pymysql.cursors.DictCursor)
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def get_list_of_top10python():
    """
    Select the top 10 countries that have Python as their most popular language.
    displays on the home screen
    """
    query = ("""SELECT country.name, country.iso2_code, languages.iso2_code, languages.language, languages.num_pushers
                FROM country
                JOIN languages ON country.iso2_code = languages.iso2_code
                WHERE languages.language = 'Python' 
                ORDER BY languages.num_pushers DESC 
                LIMIT 10;""")
    return execute_query(query)


def get_languages():
    """
    Selects and finds all the programming languages in the dataset.
    displays during user creation
    """
    query = ("""SELECT DISTINCT language
                FROM languages
                ORDER BY language;""")
    return execute_query(query)

def get_users():
    response = table.get_item(Key={"Username": ""})
    item = response.get("Item")
    return item

def add_user_to_database(username, name):
    try:
        response = table.get_item(Key={"Username": username})
        item = response.get("Item")
        if item:
            flash('User Already Exists', 'warning')
            return
    except Exception as e:
        flash('Error Adding User', 'warning')
        return

    table.put_item(
        Item={
            'Name': name,
            'Username': username
        }
    )
    flash('User Added Successfully!', 'success')


def delete_user_from_database(username):
    try:
        response = table.get_item(Key={"Username": username})
        item = response.get("Item")
        if not item:
            flash('Error Deleting User', 'warning')
            return
    except Exception as e:
        flash('Error Deleting User', 'warning')
        return

    table.delete_item(
        Key={'Username': username}
    )
    flash('User deleted successfully', 'success')


def update_fav_lang(username, lang):

    try:
        response = table.get_item(Key={"Username": username})
        item = response.get("Item")
        if not item:
            flash('Error Updating User', 'warning')
            return
    except Exception as e:
        flash('Error Updating User', 'warning')
        return

    table.update_item(
        Key={'Username': username},
        UpdateExpression='SET fav_lang = :fav_lang',
    )
    flash('User Updated', 'success')
