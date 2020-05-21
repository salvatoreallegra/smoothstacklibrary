import json
import mysql.connector


class DBConn:

    def __init__(self):
        with open('./secret.json') as f:
            data = json.load(f)

        self.__cnx  = mysql.connector.connect(user=data['user'], 
                                              password=data['password'],
                                              host=data['host'],
                                              database=data['database'])

    """
    method takes no arguments. must have se
    returns database connection object 
    """
    def getConnection(self):
        return self.__cnx

    """
    method takes no arguments 
    closes db connection
    """
    def close(self):
        self.__cnx.close()

if __name__ == "__main__":
    cnx = DBConn()
    cnx.getConnection()
    cnx.close()
