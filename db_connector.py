import pymysql
import time
import datetime

# Add a new user to db
def add_user (id,user):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='5Lh6rumTTn', passwd='ZXUyn2QkhL', db='5Lh6rumTTn')
    cursor = conn.cursor()
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    try:
        cursor.execute("INSERT into 5Lh6rumTTn.users (user_id, user_name, creation_date) VALUES (%s,%s,%s)", (id,user,timestamp))
    except pymysql.err.IntegrityError:
        return "Duplicate User ID"
    conn.commit()
    cursor.close()
    conn.close()

# Delete an existing user from db
def del_user (user):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='5Lh6rumTTn', passwd='ZXUyn2QkhL', db='5Lh6rumTTn')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM 5Lh6rumTTn.users WHERE user_id = (%s)", (user))
    conn.commit()
    cursor.close()
    conn.close()

# Updating an existing user name to db
def update_user (id,user):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='5Lh6rumTTn', passwd='ZXUyn2QkhL', db='5Lh6rumTTn')
    cursor = conn.cursor()
    cursor.execute("UPDATE 5Lh6rumTTn.users SET user_name = (%s) WHERE user_id = (%s)",(user, id))
    conn.commit()
    cursor.close()
    conn.close()

# Get an existing user name from db
def get_user (id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='5Lh6rumTTn', passwd='ZXUyn2QkhL', db='5Lh6rumTTn')
    cursor = conn.cursor()
    cursor.execute("SELECT user_name FROM 5Lh6rumTTn.users WHERE user_id = (%s)", id)
    value = cursor.fetchone()
    for r in value:
        return r
    conn.commit()
    cursor.close()
    conn.close()
