import json
import datetime

with open('app.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)

for app in json_data['content']['apartmentsforsale']:
    print(datetime.datetime.strptime(app['ad_placement_date'], "%d/%m/%Y"))

