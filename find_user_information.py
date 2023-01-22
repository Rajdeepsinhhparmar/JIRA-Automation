import requests
import json

url = "https://rajdeepsinh.atlassian.net/rest/api/3/users/search"



headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


respoence=requests.get(url,headers=headers,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
data = respoence.json()
for users in data:
  print(users)

# print(respoence.json())