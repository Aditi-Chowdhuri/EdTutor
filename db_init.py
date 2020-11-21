import sqlite3

conn = sqlite3.connect("Server_side.db")
conn.execute("CREATE TABLE PROFILE (NAME TEXT, DOB DATE, EMAIL TEXT, UNAME TEXT, PHNO TEXT, PWD TEXT, STUDENTTUTOR TEXT, BIO TEXT, PRIMARY KEY (UNAME))")
conn.execute("CREATE TABLE COURSES (COURSE_ID TEXT, CNAME TEXT, CDESC TEXT, UNAME TEXT, CURL TEXT, CIMG TEXT)")
conn.execute("CREATE TABLE FEEDBACK (COURSE_ID TEXT, UNAME TEXT, RATING INT)")
conn.execute("CREATE TABLE STUDENT_PROGRESS (COURSE_ID TEXT, UNAME TEXT, ACCURACY TEXT)")
conn.commit()
conn.close()
