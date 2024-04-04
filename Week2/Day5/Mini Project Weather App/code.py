import sqlite3
import os
# Specify the file path to the SQLite database
db_file = 'C:/Users/v_gol/anaconda3/Lib/site-packages/pyowm/commons/cityids/cities.db.bz2'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)


# # Get the absolute path to the SQLite database file
# db_file = os.path.abspath('cities.db.bz2')
#
# # Connect to the SQLite database
# conn = sqlite3.connect(db_file)