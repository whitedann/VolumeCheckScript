import os
import sspyrs
os.chdir('W:\\Employees\Danny\dev')
url = 'http://ssrsreports.idtdna.com/REPORTServer/Pages/ReportViewer.aspx?%2fManufacturing%2fSan+Diego%2fPlate+Volume+Information+by+Barcode+ID&rs:Command=Render&BarcodeID=2628529'
report = sspyrs.report(url,'dwhite','Owner4504')
report.directdown('test')
