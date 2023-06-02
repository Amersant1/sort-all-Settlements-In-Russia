from xlsxwriter import *

from kladr_base import *

import xlrd
import datetime

# import openpyxl
# Define variable to load the wookbook
# wookbook = openpyxl.load_workbook("Лист Microsoft Excel.xlsx")
# # Define variable to read the active sheet:
# worksheet = wookbook.active
# # Iterate the loop to read the cell values
# # rows=list(worksheet.rows())
# for row in worksheet.iter_rows(min_row=1, max_col=7, max_row=worksheet.max_row):    # row=worksheet.row
#     name, type, kladr_code, index, ghin,uno, is_capital = row

#     name=name.value
#     type = type.value
#     kladr_code = kladr_code.value
    
#     settlement=Settlement(Name=name,
#                           Latitude=0,
#                           Longitude=0,
#                           KladrIndex=kladr_code,
#                           Type=type)
#     Session.add(settlement)
# Session.commit()

import time
from AdrKoord import get_coordinates
punkts=Session.query(Settlement).all()
try:

    for punkt in punkts:
            if int(punkt.Latitude)==0 and int(punkt.Longitude)==0:
                name=punkt.Name
                coordinates=get_coordinates(name)
                latitude=coordinates["latitude"]
                longitude=coordinates["longitude"]
                Session.query(Settlement).filter(Settlement.Name==name).update({"Longitude":longitude,"Latitude":latitude})
                time.sleep(0.5)
except Exception as err:
    print (err)
finally:
    Session.commit()