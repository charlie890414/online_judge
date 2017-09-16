import requests 
import urllib
tmp = requests.get("https://www.dcard.tw/_api/forums/pet/posts")
raw_json = tmp.json()
key=0
for i in raw_json :  
    for j in i['media']:
        print(j['url']+' '+str(key))
        urllib.request.urlretrieve( j['url'] , "local"+str(key)+".jpg")
        key+=1