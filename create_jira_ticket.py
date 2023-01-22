import requests
import json

url = "https://rajdeepsinh.atlassian.net/rest/api/2/issue"

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

issue=json.dumps(
{
    "fields": {
       "project":
       {
          "key": "PP"
       },
       "summary": "With Assign",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "name": "Bug"
       }
   }
}
)

respoence=requests.post(url,headers=headers,data=issue,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
print(respoence.text)