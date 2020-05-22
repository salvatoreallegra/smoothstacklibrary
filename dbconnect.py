import json
import mysql.connector


class DBConn:
    # Constructor
    # Opens db Connection
    def __init__(self):
        with open('./secret.json') as f:
            data = json.load(f)

        self.__cnx = mysql.connector.connect(user=data['user'],
                                             password=data['password'],
                                             host=data['host'],
                                             database=data['database'])

    """
     Destructor
     closes db connection
    """
    def __delete__(self):
        self.__cnx.close()

    """
     method takes no arguments. must have se
     returns database connection object 
    """
    def getConnection(self):
        return self.__cnx

    def getCursor(self):
        return self.__cnx.cursor()


if __name__ == "__main__":
    cnx = DBConn()
    cnx.getConnection()
