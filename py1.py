from os import system, name 
import requests
import regex
import re
response = requests.get('https://google.com/')
x= str(response)
print (x)
x=re.findall("200", x)
if x != "":
    print ("found")
else:
    print ("not found")
