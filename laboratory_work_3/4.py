from prettytable import PrettyTable
import xml.etree.ElementTree as ET

tree = ET.parse('2.XML')
root=tree.getroot()

for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    group = info.find('group').text
    discipline = info.find('discipline').text
    total_works = info.find('total_works').text
    completed_works = info.find('completed_works').text
    x = PrettyTable()
    x.field_names = ["surname", "name", "patronymic", "group", "discipline", "total_works", "completed_works"]
    x.add_row([surname, name, patronymic, group, discipline, total_works, completed_works])
    print(x)