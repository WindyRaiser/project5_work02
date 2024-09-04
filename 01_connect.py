import mysql.connector

# Initialize a variable to hold the database connection
conn = None

try:
    # Attempt to establish a connection to the MySQL database
    conn = mysql.connector.connect(host='localhost', 
                                   port=3306,
                                   database='pub',
                                   user='<user>',
                                   password='<password>')
    
    # Check if the connection is successfully established
    if conn.is_connected():
        print('Connected to MySQL database')

except mysql.connector.Error as e:
    # Print an error message if a connection error occurs
    print(e)

finally:
    # Close the database connection in the 'finally' block to ensure it happens
    if conn is not None and conn.is_connected():
        conn.close()

# comment lien1

# 두번째 brahcn test02에서 다시 라인을 추가함.  am 11:49
#  다시 세번째로 branch 에서 작업 12:09
