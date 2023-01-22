import requests
import json

url = "https://rajdeepsinh.atlassian.net/rest/api/2/user"



headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload=json.dumps(
{
  "emailAddress": "jignesh@atlassian.com",
}
)
respoence=requests.post(url,headers=headers,data=payload,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
print(respoence.text)