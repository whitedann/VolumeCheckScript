import requests
import os
import sspyrs
import openpyxl
import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range
import getpass

#TODO: update input commands..
user = input('user: ')
password = getpass.getpass('Password: ')
barcode = input('BARCODE: ')
customer = input("Customer: ")


#Work directory
os.chdir('W:\\Employees\Danny\dev')

#Home directory
#os.chdir('C:\\Users\Dan\Desktop\idtdocs')

output1 = customer + '_' + barcode + '.xlsx'

#get template file
payload = {'username':user,'username2':'','initialRequest':'','password':password}

with requests.Session() as s:
    p = s.post('https://idtdna.mastercontrol.com/mc/login/index.cfm?action=login',data=payload)
    r = s.get('https://idtdna.mastercontrol.com/mc/Main/MASTERControl/Organizer/view_file.cfm?id=XBCYSHLULRA4XBIBB7')
    output = open('template.xlsx','wb')
    output.write(r.content)
    output.close()

#get volume file
url = 'http://ssrsreports.idtdna.com/REPORTServer/Pages/ReportViewer.aspx?%2fManufacturing%2fSan+Diego%2fPlate+Volume+Information+by+Barcode+ID&rs:Command=Render&BarcodeID='
url += barcode
report = sspyrs.report(url,user,password)
report.directdown('volumeInfo','EXCEL')

#copy data (!!change filename!!)
info = xlrd.open_workbook('volumeInfo.xls')
template = load_workbook('template.xlsx')

start = template.active
start.cell(row=1,column=2).value = barcode
start.cell(row=1,column=9).value = user
#start.close()

source = info.sheet_by_index(0)
dest = template['Raw Data']

for row in range(2,source.nrows):
    for col in range(0,6):
        dest.cell(column=col+1, row=(row-1)).value = source.cell(row,col).value

template.save(filename = output1)
#info.close
template.close()

#TODO: delete template, volumeinfo
os.remove('template.xlsx')
os.remove('volumeInfo.xls')

#open prepared file (needs to close?)
file = output1
os.startfile(file)



#run vc?

