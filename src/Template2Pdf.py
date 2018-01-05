from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template("auto-generate-pdf-list.html")

def create_pdfs(StudentsDict):
    for key, valueList in StudentsDict.items():
        create_pdf(key, valueList)


def create_pdf(directory, Students):
    """
        {
            "University": "Ytu",
            "Year": 2015,
            "Semester": "Guz",
            "CourseCode": "BLM1551",
            "Homework": "HW2",
            "StudentNumber": "1400128",
            "StudentNameSurname": "EmreGuler",
            "Time": "12.12.17",
            "Directory": "/Ytu/....."
        }
    """
    # Burda directory degiskeninide parse ederek bulabiliriz. Ama gerek yok. Cunku Students listesinin icindeki ogrencilerin hepsi ayni odevi gondermistir.
    one_student = Students[0]
    # Students dictionary'sini Time'a gore siralamaliyiz.
    html_out = template.render({
        "title" : "{} - {} - {} - {} - {} - List".format(
                one_student["University"],
                one_student["Year"],
                one_student["Semester"],
                one_student["CourseCode"],
                one_student["Homework"]
            ),
        "students": sorted(Students, key=lambda k: k['Time'])}
    )
    
    HTML(string=html_out).write_pdf(directory + "/List.pdf")