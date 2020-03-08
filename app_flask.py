# importing the requests library 
import requests 

# api-endpoint 
URL = "http://localhost:9200/test-index/_search?pretty=true"

# location given here 


# sending get request and saving the response as response object 
r = requests.get(url = URL) 

# extracting data in json format 
data = r.json() 
for hit in data['hits']['hits']:
    print("%(text)s" % hit["_source"])