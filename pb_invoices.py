import pb_auth
import requests
import datetime


url = "https://api.practicebetter.io/consultant/payments/invoices"
yesterday = datetime.date.today() - datetime.timedelta(days=1)
date_now = yesterday.isoformat()
querystring = {"invoicedate_gte":f"{date_now}T00:00:00","invoicedate_lte":f"{date_now}T23:59:59","limit":"1"}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"bearer {pb_auth.access_token}"
}

response = requests.request("GET", url, headers=headers, params=querystring)
invoice_data = response.json()

def get_id():
    for item in invoice_data['items']:
        clientRecord = item['clientRecord']
        id = clientRecord['id']
        return id

get_id()

#with open("output/invoices.txt","w") as file:
#    json.dump(invoice_data,file,indent=4)