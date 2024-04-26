import requests
from bs4 import BeautifulSoup

def get_departments(): 
    URL = "https://app.testudo.umd.edu/soc/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="course-prefix")

    dep_prefix = []
    for result in results:
        prefix = result.find("span", class_="prefix-abbrev").text
        dep_prefix.append(prefix);

    print(dep_prefix)
    return dep_prefix

def get_courses(department): 
    URL = "https://app.testudo.umd.edu/soc/202408/" + department
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    #courses = soup.find_all("div", class_="course")
    coursenames = soup.find_all("div", class_= "course-id")

    list_of_courses = []

    for course in coursenames:
        list_of_courses.append(course.text)

    print(list_of_courses);

class Department: 
    courses = [] ## 

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

#get_departments()
get_courses("CMSC");

