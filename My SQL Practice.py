# importing required libraries
import mysql.connector
  
dataBase = mysql.connector.connect(host ="localhost", user ="root", password = "Password@123", database = "mayildb")
 
# preparing a cursor object
cursorObject = dataBase.cursor()
  
# # creating table 
# studentRecord = """CREATE TABLE STUDENT (
#                    NAME  VARCHAR(20) NOT NULL,
#                    BRANCH VARCHAR(50),
#                    ROLL INT NOT NULL,
#                    SECTION VARCHAR(5),
#                    AGE INT
#                    )"""
  
# # table created
# cursorObject.execute(studentRecord) 


  
# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES %s, %s, %s"
# val = ("Sandhiya", "CSE", "85", "B", "19"),("Aisha", "ECE", "78", "A", "20"),("Suriya", "IT", "92", "C", "25")
   
# cursorObject.executemany(sql, val)
# print(sql, val)
# dataBase.commit()

Delete = "DELETE FROM student WHERE NAME='Mayil'"
cursorObject.execute(Delete)
dataBase.commit()
