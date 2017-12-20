import os
import re
import GmailApi

def get_messages_with_details(service, messages_list):
    """
        Mail yerine Message kullanmamizin sebebi google'un oyle adlandirmasindan dolayidir.
        Mail'leri daha detayli sekilde doneriz.

        {
            "University": "Ytu",
            "Year": 2015,
            "Semester": "Guz",
            "CourseCode": "BLM1551",
            "Homework": "HW2",
            "StudentNumber": "1400128",
            "StudentNameSurname": "EmreGuler",
            "Time": "",
            "Directory": "${workspaceFolder}/Ytu/2015/Guz/BLM1551/HW2"
        }
    """
    all_messages = []
    for message_obj in messages_list:
        MessageData = {}
        MessageData['MessageId'] = message_obj['id']

        message = GmailApi.get_message(service, 'me', MessageData['MessageId'])

        for header in message['payload']['headers']:
            if header['name'] == 'From':
                MessageData['From'] = header['value']
            if header['name'] == 'Subject':
                MessageData['Subject'] = header['value']
            if header['name'] == 'Date':
                MessageData['Date'] = header['value']
            if header['name'] == 'Content-Type':
                MessageData['Content-Type'] = header['value']

        MessageData['Snippet'] = message['snippet']

        # Mail kabul edilen formata uygunsa, mail listesine eklenir.
        result_mail = is_valid_mail(MessageData)
        if result_mail:
            dir_path = create_directory(result_mail)
            result_mail['MessageId'] = MessageData['MessageId']
            result_mail['From'] = MessageData['From']
            result_mail['Time'] = MessageData['Date']
            result_mail['Directory'] = dir_path
            print(result_mail)
            all_messages.append(result_mail)

    return all_messages

def is_valid_subject(subject):
    """
        Regex ile kontrol ediliyor. Eger uyusmuyorsa False, eger uyusuyorsa uyusanlar doner.
        [Ytu-2015-Guz-BLM1551-HW2-1400128-EmreGuler] konu basligini parse ederek, dictionary donucez.
        {
            "University": "Ytu",
            "Year": 2015,
            "Semester": "Guz",
            "CourseCode": "BLM1551",
            "Homework": "HW2",
            "StudentNumber": "1400128",
            "StudentNameSurname": "EmreGuler"
        }
    """
    subject_regex=r"(\w+)-(\d{4})-(\w+)-([0-9A-Z]+)-([0-9A-Z]+)-(\d+)-(\w+)"
    m = re.match(subject_regex, subject.strip('[]'))
    if m == None:
        return False
    else:
        subject_obj = {}
        subject_obj["University"] = m.group(1)
        subject_obj["Year"] = m.group(2)
        subject_obj["Semester"] = m.group(3)
        subject_obj["CourseCode"] = m.group(4)
        subject_obj["Homework"] = m.group(5)
        subject_obj["StudentNumber"] = m.group(6)
        subject_obj["StudentNameSurname"] = m.group(7)
        return subject_obj

def is_valid_mail(Mail):
    """
        Kontroller:
        Mail'in konu basligi dogru formatta mi?
        Bir sonraki versiyon, Mail'i gonderen mail adresiyle, mail'in konu kismindaki okul numarasi uyusuyor mu?
    """
    result_subject = is_valid_subject(Mail["Subject"])
    return result_subject

def create_directory(s_obj):
    """
        Suanlik dizini reponun icine olusturucak. University/Year/Semester/CourseCode/Homework
    """
    pwd = os.getcwd()
    path_list = [s_obj["University"], s_obj["Year"], s_obj["Semester"], s_obj["CourseCode"], s_obj["Homework"]]
    directory_path = pwd + "/" + "/".join(path_list)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path