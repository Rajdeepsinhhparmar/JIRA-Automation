import requests
import json
import io

url = "https://rajdeepsinh.atlassian.net/rest/api/3/issue/PP-5/attachments"

headers={
    "X-Atlassian-Token": "no-check"
}

with io.open("userlist.csv","r",encoding="utf-8") as f:
  user_data=f.read()
  f.close()

files={
    "file": user_data
}

respoence=requests.post(url,headers=headers,files=files,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
print(respoence.text)