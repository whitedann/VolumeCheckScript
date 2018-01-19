import requests

#retrieve template file
payload = {'username':'dwhite','username2':'','initialRequest':'','password':'Owner4503'}

with requests.Session() as s:
    p = s.post('https://idtdna.mastercontrol.com/mc/login/index.cfm?action=login',data=payload)
    print(p.url)

    r = s.get('https://idtdna.mastercontrol.com/mc/Main/MASTERControl/Organizer/view_file.cfm?id=XBCYSHLULRA4XBIBB7')
    output = open('test.xls','wb')
    output.write(r.content)
    output.close()
    
    
