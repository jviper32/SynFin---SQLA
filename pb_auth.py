import requests
from dotenv import load_dotenv
import os

load_dotenv()

pb_id = os.environ.get("PB_CLIENT_ID")
pb_secret = os.environ.get("PB_CLIENT_SECRET")

url = "https://api.practicebetter.io/oauth2/token"

payload = f"client_id={pb_id}&client_secret={pb_secret}"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

token = requests.request("POST",url, data=payload, headers=headers)

token_text = token.text

# TODO: how can this be done without slicing? I couldn't get the json to parse
access_token = token_text[21:-51]

print(token_text)
print(access_token)