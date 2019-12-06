#!/usr/bin/env python3
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import quote_sheetname

wb = Workbook()
dest_filename = 'test.xlsx'
ws1 = wb.active
ws1.title = "template"
ws1['A1']='type'
ws1['B1']='count'

ws2 = wb.create_sheet(title="data")
ws2['A1']='name'
ws2['A2']='dog'
ws2['A3']='cat'
ws2['A4']='bat'

dv1 = DataValidation(type="list", formula1="{0}!$A$2:$A$4".format(quote_sheetname('data')), allow_blank=True)

dv1.error ='Your entry is not in the list'
dv1.errorTitle = 'Invalid Entry'

dv1.prompt = 'Please select from the list'
dv1.promptTitle = 'List Selection'

ws1.add_data_validation(dv1)
dv1.add('A2:A4')

dv2 = DataValidation(type="whole", operator="between", formula1=0, formula2=100)

dv2.error ='Your entry is not a whole number between 0 and 100'
dv2.errorTitle = 'Invalid Entry'

dv2.prompt = 'Please enter a whole number between 0 and 100'
dv2.promptTitle = 'Count'

ws1.add_data_validation(dv2)
dv2.add('B2:B4')
wb.save(filename = dest_filename)

print('Hello World!')
