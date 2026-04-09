# dbCode.py
# Author: Your Name
# Helper functions for database connection and queries

import pymysql
import creds
import boto3

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

