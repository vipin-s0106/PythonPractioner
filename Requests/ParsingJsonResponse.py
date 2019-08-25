import requests,os,json


#Reading Json content from API and make response to json serilizable then dump into output file


response = requests.get("http://date.jsontest.com")
json_output = str(response.text)




#writing json object to JsonOutput file
json_output = json.loads(json_output.replace("\n",""))
print(json_output)

path = os.path.dirname(os.getcwd())
with open(os.path.join(path,"output/JsonOutput.json"),'w') as file:
    json.dump(json_output,file,indent=True)

    file.close()


