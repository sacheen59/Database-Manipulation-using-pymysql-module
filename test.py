import pymysql

name = input("Enter the name: ")
age = input("Enter the age: ")


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='test',
    port=3366
)

cursor = connection.cursor()

# insert data into database
try:
    cursor.execute(
    f'''
        INSERT INTO test(name,age)
        VALUES("{name}","{age}")
    '''
    )
    connection.commit()
except:
    print("Failed to insert data")

# execute select command from database
cursor.execute('SELECT * FROM test')


data = cursor.fetchall()


for row in data:
    name,age = row
    print(f"name = {name}\n age = {age}")



#close the database connection
connection.close()