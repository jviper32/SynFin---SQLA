import requests
from dotenv import load_dotenv
import os
import ast

load_dotenv()

pb_id = os.environ.get("PB_CLIENT_ID")
pb_secret = os.environ.get("PB_CLIENT_SECRET")

url = "https://api.practicebetter.io/oauth2/token"

payload = f"client_id={pb_id}&client_secret={pb_secret}"
headers = {"Content-Type": "application/x-www-form-urlencoded"}

token = requests.request("POST",url, data=payload, headers=headers)

token_text = token.text

token_dict = ast.literal_eval(token_text)
access_token = token_dict["access_token"]