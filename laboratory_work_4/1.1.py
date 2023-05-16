import json

with open('info.json', 'r', encoding="utf-8") as j:
    json_data = json.load(j)

common_count = 0
universal_count = 0

for info in json_data['content']['universalCompetencyRows']:
    if info['competence']:
        universal_count += 1

for info in json_data['content']['commonCompetencyRows']:
    if info['competence']:
        common_count += 1

print(common_count + universal_count)

