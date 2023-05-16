import json

with open('app.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)

for app in json_data['content']['apartmentsforsale']:
    print(float(app['selling_price']) / float(app['square']))