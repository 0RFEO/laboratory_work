import json

with open('app.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)

x = float(input())

for app in json_data['content']['apartmentsforsale']:
    if float(app['selling_price']) > x:
        print(str(app['address']))