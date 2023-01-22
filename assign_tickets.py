## Using this program you can assign perticular tickets to person but for this you need account id

import requests
import json

url1 = "https://rajdeepsinh.atlassian.net/rest/api/2/issue/PP-4/assignee"


headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


assign=json.dumps(
{
  "accountId": "623171e633fb8400696688af"
}
)

r2= requests.put(url1,headers=headers,data=assign,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
print(r2.text)