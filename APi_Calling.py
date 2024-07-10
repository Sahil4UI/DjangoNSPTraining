import urllib.request as url
import json
name = input("Enter Player Name : ")
path = "https://api.cricapi.com/v1/players?apikey=a7233f4d-1f47-461a-92d5-899b8409091d&offset=0&search="+name
res = url.urlopen(path)
data = json.load(res)
id = data["data"][0]["id"]
path="https://api.cricapi.com/v1/players_info?apikey=a7233f4d-1f47-461a-92d5-899b8409091d&id="+id
res = url.urlopen(path)
data = json.load(res)
print("Player Name : "+data["data"]["name"])
