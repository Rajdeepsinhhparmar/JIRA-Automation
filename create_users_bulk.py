import requests
import json
import io

url = "https://rajdeepsinh.atlassian.net/rest/api/2/user"



headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

with io.open("userlist.csv","r",encoding="utf-8") as f:
  user_data=f.read()
  f.close()

user_data=user_data.split("\n")[1:]
print(user_data)

for user in user_data:
  displayname=user.split(",")[1]
  emailAddress=user.split(",")[0]
  name=user.split(",")[1]
  payload = json.dumps(
    {
      "displayName" : displayname,
      "emailAddress": emailAddress,
      "name": name
    }
  )
  respoence=requests.post(url,headers=headers,data=payload,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
  print(respoence.text)
