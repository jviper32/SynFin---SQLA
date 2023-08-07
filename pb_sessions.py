import pb_auth
import requests
import json
import datetime


url = "https://api.practicebetter.io/consultant/sessions"
yesterday = datetime.date.today() - datetime.timedelta(days=1)
date_now = yesterday.isoformat()
querystring = {"date_gte":f"{date_now}T00:00:00","date_lte":f"{date_now}T23:59:59"}


headers = {
    "Content-Type": "application/json",
    "Authorization": f"bearer {pb_auth.access_token}",
}

print(headers)

response = requests.request("GET", url, headers=headers, params=querystring)
session_data = response.json()

with open("output/sessions.txt","w") as file:
    json.dump(session_data,file,indent=4)
