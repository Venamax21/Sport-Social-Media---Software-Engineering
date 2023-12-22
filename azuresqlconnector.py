import pyodbc

# This class manages the Azure SQL DB connection
class SQLConnection(object):
    __instance = None
    __connection = None

    def __new__(cls):
        if SQLConnection.__instance is None:
            SQLConnection.__instance = object.__new__(cls)        
        return SQLConnection.__instance  

    def getConnection(self):

        server = 'sqlserverhuelhorsttommy01.database.windows.net'
        database = 'sqldbhuelhorsttommy01'
        username = 'sqlserveradmin'
        password = 'Password123'
        driver= '{ODBC Driver 18 for SQL Server}'

        if (self.__connection == None):
            self.__connection = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        
        return self.__connection
    
    def removeConnection(self):
        self.__connection = None