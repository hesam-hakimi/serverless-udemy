import json
import boto3
import requests
import csv

SITE = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(SITE)
data = response.json()

csv_data = dict()
csv_data['date'] = data["time"]["updated"]
csv_data['cur'] = data["bpi"]["USD"]["code"]
csv_data['rate_float'] = data["bpi"]["GBP"]['rate_float']


with open('test.csv', mode='w') as csv_file:
    fieldnames = ['date', 'cur', 'rate_float']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(csv_data)
