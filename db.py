import pymysql

class Student:

    def __init__(self,id,name,surname,subject,email):
        self.id = id
        self.name = name
        self.surname = surname
        self.subject = subject
        self.email = email

    def __str__(self) -> str:
        return f"Student {str(self.id)} {self.name} {self.surname} {self.subject} {self.email}"
    

# obj = Student(
#     id=1,
#     name="Sachin",
#     surname="Barali",
#     subject="Mathematics",
#     email="baralisachin472@gmail.com"
# )

# print(obj)

# Open database


connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='students',
        port=3366
    )
cursor = connection.cursor()

    #execute sql query using execute method
cursor.execute('SELECT * FROM students')
print('cursor.rowcount',cursor.rowcount)
print('cursor.description',cursor.description)

data = cursor.fetchall()
for row in data:
    student_id,name,surname,subject,email = row
    student = Student(id=student_id,name=name,surname=surname,subject=subject,email=email)
    print(student)


# disconnect from server 
connection.close()