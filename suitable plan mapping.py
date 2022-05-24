#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      005268
#
# Created:     01/05/1479
# Copyright:   (c) 005268 1479
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import numpy

input_tb_suitable_plan = "TreeDataV2_ExcelToTable"
arr = arcpy.da.FeatureClassToNumPyArray(input_tb_suitable_plan, ('Plant_Name', 'Suggest_soil_ID'))

input_fc_suitable_plan = 'soil'
fields = ['Symbole', 'suitable_plan']
for i in range(len(arr)):

    name=arr[i][0]
    symb=arr[i][1]
    print("name={0}  and  symbol={1}".format(name,symb))

    with arcpy.da.UpdateCursor(input_fc_suitable_plan, fields) as cursor:
        for row in cursor:
            if row[0].count(symb) > 0:
                if row[1] is None:
                    row[1] = name
                elif row[1].count(name) == 0:
                    row[1] += ','+name

            # Update the cursor with the updated list
            cursor.updateRow(row)