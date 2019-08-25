import requests,os
from bs4 import BeautifulSoup

#Problem Read Times of India Headline and Print the Headline in new file name TimesOfIndia.txt

response = requests.get("https://timesofindia.indiatimes.com/home/headlines")
print("Status Code - "+str(response.status_code)+"\n\n")

#Parsing the html content
content = BeautifulSoup(response.text,'html.parser')

#Multiple Elements was there so get 2nd Element and then find again with span tag as classname w_tle
headlines = content.find_all('div',class_="news_card")[1].find_all('span',class_='w_tle')
for i in range(len(headlines)):
    print("Headline "+str(i+1)+" - "+headlines[i].get_text())


path = os.path.dirname(os.getcwd())
with open(os.path.join(path,"output/TimesOfIndia.txt"),'w') as file:
    for i in range(len(headlines)):
        file.write("Headline " + str(i + 1) + " - " + headlines[i].get_text()+"\n\n")
    file.close()
