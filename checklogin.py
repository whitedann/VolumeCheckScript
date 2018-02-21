import requests
import os

os.chdir('W:\\Employees\Danny\dev')


def getTemplate():
    payload = {'username':'dwhite323','username2':'','initialRequest':'','password':'Owner4504'}

    with requests.Session() as s:
        p = s.post('https://idtdna.mastercontrol.com/mc/login/index.cfm?action=login',data=payload)
        print(p)
        r = s.get('https://idtdna.mastercontrol.com/mc/Main/MASTERControl/Organizer/view_file.cfm?id=XBCYSHLULRA4XBIBB7')
        print(r)
        output = open('template.xlsx','wb')
        if len(r.content) < 10000:
           print('could not connect to MC')
        else:
            output.write(r.content)
            output.close()
            print('success')
        
            
    return;

getTemplate()
