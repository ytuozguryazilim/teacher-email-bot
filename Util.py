import os
import re

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