import requests
from bs4 import BeautifulSoup
import json

def get_departments(): 
    URL = "https://app.testudo.umd.edu/soc/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="course-prefix")

    for result in results:
        prefix = result.find("span", class_="prefix-abbrev").text

        with open('course_data.json','r+') as file:
            file_data = json.load(file)
            file_data[prefix] = []
            file.seek(0)
            json.dump(file_data, file, indent = 4)

        write_courses(prefix)


def write_courses(department): 

    APIURL = 'https://api.umd.io/v1/courses?dept_id=%s'
    courses = requests.get(url = APIURL % department).json()

    for course in courses:
        imp_data = {}
        imp_data["course_id"] = course["course_id"]
        imp_data["sections"] = course["sections"]

        with open('course_data.json','r+') as file:
            file_data = json.load(file)
            file_data[department].append(imp_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        
        for section in course["sections"]:
            write_times_and_instructors(department, section)


def write_times_and_instructors(department, section_id):
    APIURL = 'https://api.umd.io/v1/courses/sections/%s'
    section = requests.get(url = APIURL % section_id).json()
    
    imp_data = {}
    imp_data["meetings"] = section["meetings"]
    imp_data["instructors"] = section["instructors"]

    with open('course_data.json','r+') as file:
            file_data = json.load(file)
            file_data[department][section_id].append(imp_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

def main():
    get_departments()


if __name__ == '__main__':
    main()



