#Airtable Bulk Download Attachments
#How do you export attachments from Airtable ?
#Mass download attachments from Airtable ?
#Airtable-Bulk-Attachments-Downloader
#Airtable Bulk Attachments Download using python
#Use this script to bulk download all Airtable attachments no matter how big they are.

import requests
import json

base_id = "<<YOUR BASE ID>>"
table_id = "<<YOUR TABLE ID>>"
url = "https://api.airtable.com/v0/" + base_id + "/" + table_id

api_key = "<<YOUR API KEY>>"
headers = {"Authorization": "Bearer " + api_key}

params = ()
airtable_records = []
run = True
i = 0
while run is True:
  URL = "" 
  response = requests.get(url, params=params, headers=headers)
  airtable_response = response.json()
  #print(response.json())
  airtable_records += (airtable_response['records']) 

  # record no 4  
  #print(airtable_response['records'][4]['fields']['ss'][0]['url'])
  
  #records = list(airtable_response['records'])
  #airtable_records.append(records)

  for i in airtable_response['records']:
    #print(i)
    #print(i['fields'])

    #Your attachment Field name ss was my attachment field name
    if child := i['fields'].get("ss"): 
        #print(i['fields'].get("Notes").replace(" ", ""))
        #replace with the filename with Notes field
        filename = i['fields'].get("Notes").replace(" ", "")
        print(filename) 
        print(child[0]['url'])
        #get the original image url
        URL = child[0]['url']
        response = requests.get(URL)
        open(filename+".jpg", "wb").write(response.content)

  # as Airtabel get 100 records a time, so more then 100 records need to set this
  if 'offset' in airtable_response:
     run = True
     params = (('offset', airtable_response['offset']),)
  else:
     run = False
     
#print(airtable_records)
