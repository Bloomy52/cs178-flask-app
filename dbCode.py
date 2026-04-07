# dbCode.py
# Author: Your Name
# Helper functions for database connection and queries

import pymysql
import creds

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
    query = ("""SELECT country.name, country.iso2_code, languages.iso2_code, languages.language, language.num_pushers
                FROM country, languages
                JOIN languages ON country.iso2_code = languages.iso2_code
                WHERE languages.language = 'Python' 
                ORDER BY languages.num_pushers DESC 
                LIMIT 10;""")
    return execute_query(query)



