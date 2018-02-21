import sys
sys.stdout.write('Loading dependencies..')

import requests
import os
import sspyrs
import openpyxl
import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range
import getpass

print('done!')
print('w:\\Employees\\Danny\dev for more info\n')


def start():
    global user
    global password
    global barcode
    global customer
    user = input('type user (don\'t scan badge): ')
    password = getpass.getpass('type password (hidden): ')
    barcode = input('Enter BARCODE: ')
    customer = input('Enter Customer (optional): ')
    
    #Work directory
    os.chdir('W:\\Employees\Danny\dev')

    #Home directory
    #os.chdir('C:\\Users\Dan\Desktop\idtdocs')
    return;

#get template file
def getTemplate():
    payload = {'username':user,'username2':'','initialRequest':'','password':password}

    with requests.Session() as s:
        p = s.post('https://idtdna.mastercontrol.com/mc/login/index.cfm?action=login',data=payload)
        r = s.get('https://idtdna.mastercontrol.com/mc/Main/MASTERControl/Organizer/view_file.cfm?id=XBCYSHLULRA4XBIBB7')
        output = open('template.xlsx','wb')
        output.write(r.content)
        output.close()
    return;

#get volume file
def getVolumeInfo():
    url = 'http://ssrsreports.idtdna.com/REPORTServer/Pages/ReportViewer.aspx?%2fManufacturing%2fSan+Diego%2fPlate+Volume+Information+by+Barcode+ID&rs:Command=Render&BarcodeID='
    url += barcode
    report = sspyrs.report(url,user,password)
    report.directdown('volumeInfo','EXCEL')
    return;

#copy data
def copyData():
    global output1
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

    output1 = customer + '_' + barcode + '.xlsx'
    template.save(filename = output1)
    template.close()
    return;
    
start()
getTemplate()
getVolumeInfo()
copyData()

os.remove('template.xlsx')
os.remove('volumeInfo.xls')

file = output1
os.startfile(file)


