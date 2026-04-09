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

def get_top_country(username):
    """
    Select the top country based on the user's favorite language.
    displays on the find_country.html screen.
    """

    try:
        response = table.get_item(Key={"username": username})
        item = response.get("Item")
        if not item:
            flash('Error Getting User', 'error')
            return None
    except Exception as e:
        flash('Error Getting Top Country', 'error')
        return None

    response = table.get_item(Key={"username": username})
    item = response.get("Item")
    fav_lang = item["fav_lang"]

    query = ("""SELECT country.name
                FROM country
                JOIN languages ON country.iso2_code = languages.iso2_code
                WHERE languages.language = %s 
                ORDER BY languages.num_pushers DESC 
                LIMIT 1;""")
    return execute_query(query, (fav_lang,))
# GitHub Copilot fixed the portion with the %s and the fav_lang argument

def get_languages():
    """
    Selects and finds all the programming languages in the dataset.
    displays during user creation
    """
    query = ("""SELECT DISTINCT language
                FROM languages
                ORDER BY language;""")
    return execute_query(query)

def get_fav_lang(username):
    try:
        response = table.get_item(Key={"username": username})
        item = response.get("Item")
        if not item:
            flash('Error Updating User', 'error')
            return None
    except Exception as e:
        flash('Error Updating User', 'error')
        return None

    response = table.get_item(Key={"username": username})
    item = response.get("Item")
    fav_lang = item["fav_lang"]
    return fav_lang



def add_user_to_database(username, name):
    try:
        response = table.get_item(Key={"username": username})
        item = response.get("Item")
        if item:
            flash('User Already Exists', 'error')
            return
    except Exception as e:
        flash('Error Adding User', 'error')
        return

    table.put_item(
        Item={
            'username': username,
            'name': name
        }
    )
    flash('User Added Successfully!', 'success')


def delete_user_from_database(username):
    try:
        response = table.get_item(Key={"username": username})
        item = response.get("Item")
        if not item:
            flash('Error Deleting User', 'error')
            return
    except Exception as e:
        flash('Error Deleting User', 'error')
        return

    table.delete_item(
        Key={'username': username}
    )
    flash('User deleted successfully', 'success')


def update_fav_lang(username, lang):

    try:
        response = table.get_item(Key={"username": username})
        item = response.get("Item")
        if not item:
            flash('Error Updating User', 'error')
            return
    except Exception as e:
        flash('Error Updating User', 'error')
        return

    table.update_item(
        Key={'username': username},
        UpdateExpression='SET fav_lang = :fav_lang',
        ExpressionAttributeValues={':fav_lang': lang}
    )
    flash('User Updated', 'success')
