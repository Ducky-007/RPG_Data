# STEP 0 - import sqlite3
import sqlite3
import queries as q

# STEP 1- connect to the database
# triple check spelling of database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# STEP 2- create the 'cursor'
cursor = connection.cursor()

# STEP 3- write a query
# see the queries.py file

# STEP 4- execute the query on the cursor and fetch the results
# also called 'pulling the results'
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])