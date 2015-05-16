import urllib.request
import json
from pprint import pprint
import urllib
while(True):
    try:
        
        code = input("Enter the country code (enter 'quit' to quit):")
        if (code == "quit"):
            break
        else:
            url="https://restcountries.eu/rest/v1/alpha/"+code
            page=urllib.request.urlopen(url)
            content=page.read()
            content_string = content.decode("utf-8")
            json_data = json.loads(content_string)
     #       pprint(json_data)
            print(json_data["name"])
            print(json_data['capital'])

    except urllib.error.HTTPError:
        print ("1111111")


    except Exception as e:
        print(type(e))
        print("The website is not exist!")
        

    
 
    
