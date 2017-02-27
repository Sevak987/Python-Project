import requests
import json

value1=raw_input("Dwse faghto:    ")
payload={'q':value1}
i= requests.get("http://food2fork.com/api/search?key=d480341619fadca5e4a9e50ae9fb0411",params=payload)

data= i.json()

field_list=data["recipes"]

for f in field_list:
	
	id=f["recipe_id"]
	payload1={'rId':id}
	o=requests.get("http://food2fork.com/api/get?key=d480341619fadca5e4a9e50ae9fb0411",params=payload1)
	data1=json.dumps(o.json(), indent=4, separators=(',', ': '))
	print data1

payload1={'food_pairing':value1}
i= requests.get("https://api.punkapi.com/v2/beers",params=payload1)
data2=json.dumps(i.json(), indent=4, separators=(',', ': '))

print data2
	
	
