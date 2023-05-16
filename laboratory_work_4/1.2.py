import json

with open('info.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)


for info in json_data['content']['professionalStandards']:
    print(str(info['id']), str(info['content']))
