from pickletools import float8
from tokenize import Double
import pyodbc
import pandas as pd
server = 'dbconfiguarationserver.database.windows.net'
database = 'DB_tree_data'
username = 'adminSQL'
password = '{P@ssw0rd}'   
driver= '{ODBC Driver 17 for SQL Server}'

data = []
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        query = "SELECT TOP (1000) [Plant_name], [shaped_area_wide],[shaped_area_height],[trees_per_Rai],[CO2_Absorption_(ton/rai/anual)],[CO2_Absorption(kg/rai/anual)],[CO2_Absorption(credits/m2/anual)],[CO2_Absorption(credits/tree/anual)] FROM [dbo].[Tree_data]"
        cursor.execute(query)
        row = cursor.fetchone()
        cols = ['Plant_name', 'shaped_area_wide', 'shaped_area_height', 'trees_per_Rai', 'CO2_Absorption_(ton/rai/anual)', 'CO2_Absorption(kg/rai/anual)', \
            'CO2_Absorption(credits/m2/anual)', 'CO2_Absorption(credits/tree/anual)']
        while row:
            # d = {}
            # for i in range (len(row)):
            #     if (cols[i]=='Plant_name'):
            #         d[cols[i]] = str(row[i])
            #     else:
            #         d[cols[i]] = float("{:.6f}".format(row[i]))
            # data.append(d)
            word = ''
            for i in range (len(row)):
                word += str(row[i]) + "\t"
            word += "\n"
            print(word)
            row = cursor.fetchone()

df = pd.DataFrame(data)
print(df)