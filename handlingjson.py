import json

dict1={                        #JSON (JavaScript Object Notation  Key:Value pair)
    "Sanskar":1,
    "Aditya":2,
    "Shahid":3
}

# file=open("handlingjson.json","w")
# file.writelines(dict1)
# file.close()
with open("handlingjson.json","w") as file:
    json.dump(dict1,file,indent=4)