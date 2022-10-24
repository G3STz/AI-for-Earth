import pyodbc
from iconfiguration import *

cfg = iconfiguration()

class AzureCloudDBContext:
    def __init__(self):
        self.host = cfg["db_server"]
        self.db = cfg["db_database"]
        self.user = cfg["db_username"]
        self.password = cfg["db_password"]
        self.driver = cfg["db_driver"]

    def __connect__(self):
        self.conn = pyodbc.connect('DRIVER='+self.driver+';SERVER=tcp:'+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cur = self.conn.cursor()

    def __disconnect__(self):
        self.conn.close()

    def execute(self, sql):
        result = 0
        self.__connect__()
        self.cur.execute(sql)
        row = self.cur.fetchone()
        while row:
            result = row
            row = self.cur.fetchone()
        self.conn.commit()
        self.__disconnect__()
        return result

    def execute_all(self, sql):
        result = 0
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.conn.commit()
        self.__disconnect__()
        return result