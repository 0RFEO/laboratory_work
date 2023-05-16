import xml.etree.ElementTree as ET

tree = ET.parse('1.XML')
root=tree.getroot()
print("Привет, учитель!\nПеред вами список и баллы студентов для удобной проверки, удачи!")

for student in root.findall("result/applicant"):
    surname = student.find('surname').text
    math = student.find('math').text
    russian = student.find('russian').text
    infotmatics = student.find('infotmatics').text
    id = student.get('code')
    print(surname, math, russian, infotmatics, id)

'''1.1'''
print()
print("Ответ на задание 1.1")
for student in root.findall("result/applicant"):
    surname = student.find('surname').text
    math = student.find('math').text
    russian = student.find('russian').text
    infotmatics = student.find('infotmatics').text
    id = student.get('code')
    print(int(math) + int(russian) + int(infotmatics))

'''1.2'''
print()
print("Ответ на задание 1.2")
for student in root.findall("result/applicant"):
    surname = student.find('surname').text
    math = student.find('math').text
    russian = student.find('russian').text
    infotmatics = student.find('infotmatics').text
    id = student.get('code')
    print("max " + surname, max(int(math), int(russian), int(infotmatics)))
    print("min " + surname, min(int(math), int(russian), int(infotmatics)))

'''1.3'''
print()
print("Ответ на задание 1.3")
for student in root.findall("result/applicant"):
    surname = student.find('surname').text
    math = student.find('math').text
    russian = student.find('russian').text
    infotmatics = student.find('infotmatics').text
    id = student.get('code')
    sum = (int(math) + int(russian) + int(infotmatics))
    if (sum > 250):
        print(surname)

'''1.4'''
print()
print("Ответ на задание 1.4")
for student in root.findall("result/applicant"):
    surname = student.find('surname').text
    math = student.find('math').text
    russian = student.find('russian').text
    infotmatics = student.find('infotmatics').text
    id = student.get('code')
    if (int(math) > 50) and (int(russian) > 50) and (int(infotmatics) > 50):
        print(surname)


