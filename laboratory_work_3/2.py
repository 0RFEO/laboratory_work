import xml.etree.ElementTree as ET

tree = ET.parse('2.XML')
root=tree.getroot()
print("Привет, учитель!\nПеред вами информация для удобной проверки, удачи!")

for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    group = info.find('group').text
    discipline = info.find('discipline').text
    total_works = info.find('total_works').text
    completed_works = info.find('completed_works').text
    print(surname, name, patronymic, group, discipline, total_works, completed_works)

'''2.1'''
print()
print("Ответ на задание 2.1")
for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    print(surname, name[:1] + "." + patronymic[:1])

'''2.2'''
print()
print("Ответ на задание 2.2")
for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    group = info.find('group').text
    discipline = info.find('discipline').text
    total_works = info.find('total_works').text
    completed_works = info.find('completed_works').text
    if (int(total_works) - int(completed_works) == 0):
        print(surname, "выполнил все работы")
    else:
        print(surname, "невыполнил", int(total_works) - int(completed_works))

'''2.3'''
print()
print("Ответ на задание 2.3")
for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    group = info.find('group').text
    discipline = info.find('discipline').text
    total_works = info.find('total_works').text
    completed_works = info.find('completed_works').text
    a = int(completed_works) / int(total_works)
    b = a * 100
    print(surname, "готов на", str(b) + "%")

'''2.4'''
print()
print("Ответ на задание 2.4")
for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    group = info.find('group').text
    discipline = info.find('discipline').text
    total_works = info.find('total_works').text
    completed_works = info.find('completed_works').text
    a = int(total_works) - int(completed_works)
    b = a * 10
    print(surname, "разницa в процентах между количеством выполненных работ и количеством защищенных работ", str(b) + "%")

'''2.5'''

print()
print("Ответ на задание 2.5")
for info in root.findall("student/applicant"):
    surname = info.find('surname').text
    name = info.find('name').text
    patronymic = info.find('patronymic').text
    group = info.find('group').text
    discipline = info.find('discipline').text
    total_works = info.find('total_works').text
    completed_works = info.find('completed_works').text
    a = int(total_works) - int(completed_works)
    b = a * 10
    if (b > 50):
        print(surname, "разницa в процентах между количеством выполненных работ и количеством защищенных работ", str(b) + "%", "это больше 50%. Постарайся сделать больше, а то получишь неут!")
