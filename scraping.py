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

    return dep_prefix

def get_courses(department): 
    URL = "https://app.testudo.umd.edu/soc/202408/" + department
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="course-info")
    courses = []
    for result in results:
        course_num = result.find("span", class_="course-id").text
        course_name = result.find("span", class_="course-title").text
        course_credits = result.find("span", class_="course-min-credits").text
        course = Course(course_num, course_name, course_credits)
        courses.append(course)

    return courses

class Department: 
    courses = [] ## 

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses



class Course: 

