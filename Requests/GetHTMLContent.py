import requests,os

response = requests.get("https://xkcd.com/353/")
print(response.headers) # will print the header of the response
print("#####################################")
print(response.content) #content will print byte object in the form of string
print("#####################################")
print(response.text) # text will print the string object

path = os.path.dirname(os.getcwd())
with open(os.path.join(path,"output/content.html"),"w") as file:
    file.write(response.text)
file.close()