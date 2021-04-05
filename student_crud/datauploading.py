import psycopg2
import pandas as pd  

conn = psycopg2.connect(
    host="127.0.0.1",
    database="studentdb",
    user="rahul",
    password="123456")

cursor = conn.cursor()

df = pd.read_excel('data.xls')

for index, row in df.iterrows():
    name        = row['Name']
    print('name', name)
    password    = row['Password']
    print('password', password)
    email       = row['Email']
    print('email', email)



    sql = "insert into public.crud_student (name, password, email) VALUES (%s, %s, %s)"
    val  = (name, password, email)
    cursor.execute(sql, val)
    conn.commit()

 
    
