from .azurecloud_dbcontext import AzureCloudDBContext
from .tree_translate import *
import pandas as pd
import math

df = pd.read_excel('./services/data.xlsx', sheet_name='Data')

class Calculations:
    def __init__(self):
        self.az = AzureCloudDBContext()

    def get_area_rai(self, area, unit):
        sq_meters = 0
        rai = 0
        if (unit == "km"):
            sq_meters = area * 1000
        else:
            sq_meters = area
        
        rai = round(sq_meters / 1600, 6)
            
        return float(rai)

    def get_tree_per_rai_count(self, tree_list: list) -> dict:
        tree_size_dict = {}
        # query = '''
        # SELECT trees_per_Rai 
        # FROM [dbo].[Tree_data]
        # WHERE'''
        # for name in tree_list:
        #     where_filter = ' [Plant_name] = \'' + name + '\''
        #     trees_per_Rai = self.az.execute(query + where_filter)
        #     tree_size_dict[name] = trees_per_Rai[0]
        for name in tree_list:
            tree_size_dict[name] = df[df['Plant_name'] == name]['trees_per_Rai']

        return tree_size_dict

    def get_carbon_credit(self, tree_name: list) -> dict:
        tree_carbon_dict = {}
        # query = '''
        # SELECT [CO2_Absorption(credits/tree/anual)]
        # FROM [dbo].[Tree_data]
        # WHERE'''
        # for name in tree_name:
        #     where_filter = ' [Plant_name] = \'' + name + '\''
        #     carbon_absorb = self.az.execute(query + where_filter)
        #     tree_carbon_dict[name] = carbon_absorb[0]
        for name in tree_name:
            tree_carbon_dict[name] = df[df['Plant_name'] == name]['CO2_Absorption(credits/tree/anual)']
        return tree_carbon_dict

    def calc(self, tree_list, area, unit) -> dict:
        rai = self.get_area_rai(area, unit)
        tree_per_rai = self.get_tree_per_rai_count(tree_list=tree_list)
        tree_carbon = self.get_carbon_credit(tree_name=tree_list)

        res = []

        for k, v in tree_per_rai.items():
            t = {}
            t["plant_name"] = k
            plant_count = math.floor(float(tree_per_rai[k]) * rai)
            t["total"] = plant_count
            t["carbon_credit"] = round(plant_count * float(tree_carbon[k]), 4)
            res.append(t)

        # DataFrame is used for sorted only, df can be changed to others structure in the future
        df = pd.DataFrame.from_dict(res)
        df = df.sort_values(by='carbon_credit', ascending=False)
        
        result = df.to_dict('records')
        return result
        # return dict(sorted(res.items(), key = lambda x: x[1], reverse = True))  # desc
        

# c = Calculations()
# s = c.calc(['ปาล์มน้ำมัน','กระถินณรงค์',], 1, 'm')
# print(s)
