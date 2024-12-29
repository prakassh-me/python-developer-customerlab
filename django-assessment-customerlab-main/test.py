import requests
import json
import random, string
webhook_url = "http://127.0.0.1:8000/webhook/"


email_id = input("Enter email_id: ")
acc_nme = input ("Please enter you account name: ")

app_secret_token = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=20))


data = {}

data["email_id"] = email_id
data["acc_nme"] = acc_nme
data["CL-X-TOKEN"] = app_secret_token

print(data)

r = requests.post(webhook_url, data = json.dumps(data), headers={'Content-Type': 'application/json'})
