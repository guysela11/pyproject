import pymysql
import requests

def res1():
    res = requests.post('http://127.0.0.1:5000/users/1', json={'user_name':"John"})
    if res.ok:
        print(res.json())

def res2():
    res = requests.get('http://127.0.0.1:5000/users/1')
    if res.ok:
        print(res.json())

def res3():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='5Lh6rumTTn', passwd='ZXUyn2QkhL', db='5Lh6rumTTn')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 5Lh6rumTTn.users WHERE user_id = (%s)", 1)
    value = cursor.fetchall()
    for r in value:
        print (r)
    conn.commit()
    cursor.close()
    conn.close()

res1()
res2()
res3()