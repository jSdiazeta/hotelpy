import mysql.connector as connector
def connect():
    mydb = connector.connect(host='localhost',user='root',passwd='9947665213',database='hotel_')
    #print('....connection established ', mydb,'....\n')
    return mydb






