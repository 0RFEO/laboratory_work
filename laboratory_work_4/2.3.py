import json

with open('app.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)

for app in json_data['content']['apartmentsforsale']:
    if (app['floor'] == "2" and float(app['square']) > 40):
        print(str(app['address']))