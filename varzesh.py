import requests
from bs4 import BeautifulSoup

web=requests.get("https://varzesh3.com")
soup=BeautifulSoup(web.content)
dvs=soup.find_all("div")
dvs=soup.find_all("div",{"class":"news-main-list"})
links=dvs[0].find_all("a")+dvs[1].find_all("a")
ns=[]
ms=[]
for link in links:
    if "https://video.varzesh3.com/video/" in link["href"]:
        ns.append(" ")
    else:
        ms.append(link["href"]+"\n")

for m in ms:
    web=requests.get(m)
    soup=BeautifulSoup(web.content)
    dvs=soup.find_all("div",{"class":"news-main-image"})
    if dvs != []:
     img=dvs[0].find_all("img")[0]["src"]
     n=img.strip().split("/")[-1].strip().split("?")[0]
     f2=open("images/" +n ,"wb")
     web=requests.get(img)
     f2.write(web.content) 
     f2.close()  