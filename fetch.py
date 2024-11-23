import requests
from bs4 import BeautifulSoup as beauty
import pymysql
import json

# set the url
url = "https://jsonplaceholder.typicode.com/comments"

# fetch the data 
response = requests.get(url)
data = response.json()



#open the database

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='db_comment',
    port=3366
)

cursor = connection.cursor()

table_name = "tb_comment"
fields = """
    id INT PRIMARY KEY,
    postId INT,
    name TEXT,
    email VARCHAR(255),
    body TEXT
"""

# create table query
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields});"

cursor.execute(create_table_query)

for i in range(len(data)):
    cursor.execute(
        f"""
            INSERT INTO {table_name}(id,postId,name,email,body)
            VALUES("{data[i]['id']}","{data[i]['postId']}","{data[i]['name']}","{data[i]['email']}","{data[i]['body']}");
        """
    )
    connection.commit()

#close the connection of database
connection.close()




