class Department: 
    ## name-> string
    ## courses -> Course[]
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

class Course: 
    ## course_name -> string 
    ## sections -> Sections[]
    def __init__(self, course_name, sections):
        self.course_name = course_name
        self.sections = sections

class Section: 
    ## section_num -> num
    ## professor_name -> string
    def __init__(self, section_num, professor_name):
        self.section_num = section_num
        self.professor_name = professor_name