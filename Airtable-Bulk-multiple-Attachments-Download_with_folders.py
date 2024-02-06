#Airtable Bulk Download Attachments
#How do you export attachments from Airtable ?
#Mass download attachments from Airtable ?
#Airtable-Bulk-Attachments-Downloader
#Airtable Bulk Attachments Download using python
#Use this script to bulk download all Airtable attachments no matter how big they are.

import requests
import json
import os

base_id = "<<YOUR BASE ID>>"
table_id = "<<YOUR TABLE ID>>"
url = "https://api.airtable.com/v0/" + base_id + "/" + table_id

api_key = "<YOUR API KEY>>"
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
  #print(airtable_response['records'][4]['fields']['PPT'][0]['url'])
  
  #records = list(airtable_response['records'])
  #airtable_records.append(records)

  os.makedirs('PPT', exist_ok=True)     
  os.makedirs('PDF', exist_ok=True) 

  for i in airtable_response['records']:
    #print(i)
    #print(i['fields'])

    #Your attachment Field name PPT & PDF was my attachment field name
    if child := i['fields'].get("PPT"): 
        #print(i['fields'].get("Notes").replace(" ", ""))
        #replace with the filename with Notes field
        filename = i['fields'].get("Company Name").replace(" ", "")
        print(filename) 
        ##All information with the attachement
        #print(child[0])
        
        #print(child[0]['url'])
        #get the original image url
        #print(len(child))
        dd = 0
        for a in child:
            URL = child[dd]['url']
            print(child[dd]['url'])
            #print(dd)
            response = requests.get(URL)
            ##Change the filename
            #open(os.path.join('PPT',(filename+".png")), "wb").write(response.content)
            path = 'PPT\\' + filename
            os.makedirs(path, exist_ok=True)
            ##using the existing filename
            open(os.path.join(path,(child[dd]['filename'])), "wb").write(response.content)
            dd = dd + 1
        
    if child := i['fields'].get("PDF"): 
        #print(i['fields'].get("Notes").replace(" ", ""))
        #replace with the filename with Notes field
        ff = 0
        for b in child:
            filename = i['fields'].get("Company Name").replace(" ", "") + str(ff)
            print(filename) 
            print(child[ff]['url'])
            #get the original image url
            URL = child[ff]['url']
            response = requests.get(URL)
            open(os.path.join('PDF',(filename+".png")), "wb").write(response.content)
            ff = ff + 1

  # as Airtabel get 100 records a time, so more then 100 records need to set this
  
  if 'offset' in airtable_response:
     run = True
     params = (('offset', airtable_response['offset']),)
  else:
     run = False
     
#print(airtable_records)
