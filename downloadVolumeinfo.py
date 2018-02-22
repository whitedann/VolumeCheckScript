import os
import sspyrs
import xlrd
os.chdir('W:\\Employees\Danny\dev')
url = 'http://ssrsreports.idtdna.com/REPORTServer/Pages/ReportViewer.aspx?%2fManufacturing%2fSan+Diego%2fPlate+Volume+Information+by+Barcode+ID&rs:Command=Render&BarcodeID=2630747'
report = sspyrs.report(url,'dwhite','Owner4504')

try:
    report.directdown('test','EXCEL')
except ValueError:
    print('\n\nFailed to download volume file. Check that barcode is correct.\n')

info = xlrd.open_workbook('test.xls')
source = info.sheet_by_index(0)

checkString = source.cell(0,0).value
delimitedString = checkString.split(' ')
if(delimitedString[8] == ''):
    print('invalid barcode')
else:
    print('valid barcode')

    
