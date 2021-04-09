import requests
from bs4 import BeautifulSoup
import ctypes
from datetime import datetime, timedelta

def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

url = "https://forums.ea.com/en/commandandconquer/categories/news-announcements"
keys = ["new", "world starting"]

newWorlds = []
newDates = []

Mbox("test", "run", 0)

#get latest detected world
try:
    file = open("data.dat", 'r')
    latestWorld = file.read()
    file.close()
except FileNotFoundError:
    now = datetime.now()-timedelta(days=50)
    latestWorld = now.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    file = open("data.dat", 'w')
    file.write(latestWorld)
    file.close()

try:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    #posts = soup.findAll('a', attrs = {'class':'Title'})


    trs = soup.findAll('tr', attrs = {'class':'ItemDiscussion'})

    for tr in trs:
        postTitle = tr.findAll('a', attrs = {'class':'Title'})[0].getText()
        postDate = tr.findAll('a', attrs = {'class':'CommentDate'})[0].find('time').get('datetime')

        KeysPresent = True
        text = postTitle
        for subkey in keys:
            KeysPresent = KeysPresent & (subkey in text.lower())

        if KeysPresent:
            if postDate > latestWorld:
                newWorlds.append(postTitle)
                newDates.append(postDate)
    
    for i in range(0, len(newWorlds)):
        print(newWorlds[i] + ': ' + newDates[i])
    
    #forum always ordered from latest post down. Hence the first element in the list will always be the most recent world!
    if len(newWorlds) > 0:
        with open("data.dat", 'w') as file: 
            file.write(newDates[0])
        text = '\n'.join(newWorlds)
        Mbox("New Tiberium Alliance Worlds", text ,0)

except Exception as e:
    print(e)
