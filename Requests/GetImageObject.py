import requests,os

# As image is object so take as write byte object thats why content is used bcz it will return the byte object
response = requests.get("https://imgs.xkcd.com/comics/python.png")
path = os.path.dirname(os.getcwd())
with open(os.path.join(path,"output/img.jpg"),"wb") as file:
    file.write(response.content)