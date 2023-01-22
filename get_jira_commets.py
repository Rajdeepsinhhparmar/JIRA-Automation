## Using this program you can get JIRA commets from specific tickets.
import requests
import json

url = "https://rajdeepsinh.atlassian.net/rest/api/3/issue/PP-2/comment"



headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


respoence=requests.get(url,headers=headers,auth=("rajdeepparmar79201@gmail.com", "cNQQRqd2SnUFRfjwbUCF50C9"))
data = respoence.json()
# print(data)


h = (data["total"])   # get total comment count from tickets
print(h)
# print(data["comments"][0]["id"])  # comment id

# print(data["comments"][0]["body"]["content"][0]["content"][0]["text"])

a= (data["comments"][2]["body"]["content"])
# print(a)
print(len(a))
#
# i =0
# for i in range(len(a)):
#   print(data["comments"][0]["body"]["content"][i]["content"][0]["text"])


for comments in data["comments"]:
    print(f'comment id is:{comments["id"]}')
    for i in range(len(a)):
        print(f'comment text is:{comments["body"]["content"][i]["content"][0]["text"]}')



    # for j in data["comments"]:
    #     a = (data["comments"][j]["body"]["content"])
    #     for i in range(len(a)):
    #         print(data["comments"][j]["body"]["content"][i]["content"][0]["text"])



