import names
import random
import string
import csv
import matplotlib.pyplot as plt

class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        my_sum = 0
        for grade in self.data_sheet.get_grades_as_list():
            my_sum += int(grade)
        avg_grade = my_sum / len(self.data_sheet.get_grades_as_list())
        return avg_grade

    def get_progression(self):
        total_etsc = 0
        for course in self.data_sheet.courses:
            total_etsc += int(course.ETSC)
        progression = total_etsc / 150
        return progression

        
        

class DataSheet():
    def __init__(self, courses = []):
        self.courses = courses

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades



class Course(): 
    def __init__(self,name, classroom, teacher, ETSC, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETSC = ETSC
        self.grade = grade



def generate_students(number):
    course_names = ["Secruity", "Typescript", "Kotlin"]
    genders = ["male", "female"]
    grades = ["-3","00","02", "4", "7","10","12"]
    
    
    for x in range(0,number):
        with open("./modules/week3.csv", "a") as file_obj:
            name = names.get_full_name()
            image_url = ''.join(random.choice(string.ascii_lowercase) for i in range(15))
            course = Course(random.choice(course_names), "D klassen", "Thomas", "20", random.choice(grades))
            data_sheet = DataSheet([course])
            student = Student(name, random.choice(genders), data_sheet, image_url)
            text_to_file= "name: {stud_name}, course name: {course_name}, teacher: {teacher}, etsc: {etsc}, classroom: {classroom}, grade: {grade}, image_url: {image_url}, gender: {gender}" .format(stud_name = student.name, course_name = course.name, teacher = course.teacher, etsc = course.ETSC, classroom = course.classroom, grade = course.grade, image_url = student.image_url, gender = student.gender)

            file_obj.write(text_to_file + "\n")

def get_students_list():
    student_list = []
    with open("./modules/week3.csv") as file_obj:
        lines = file_obj.readlines()
        for line in lines:
          name = (line.split("name: "))[1].split(",")[0]   
          course_name = (line.split("course name: "))[1].split(",")[0]
          teacher = (line.split("teacher: "))[1].split(",")[0]
          etsc = (line.split("etsc: "))[1].split(",")[0]
          classroom = (line.split("classroom: "))[1].split(",")[0]
          grade = (line.split("grade: "))[1].split(",")[0]
          image_url = (line.split("image_url: "))[1].split(",")[0]
          gender = (line.split("gender: "))[1].split(",")[0]  

          course = Course(course_name, classroom, teacher, etsc, grade)
          data_sheet = DataSheet([course])
          student = Student(name, gender, data_sheet, image_url)
          student_list.append(student)
    return student_list 
          
          
    
def print_students():
    student_list = get_students_list()
    for student in student_list:
        text = "name: {stud_name}, image_url: {image_url}, avg_grade: {avg_grade}".format(stud_name = student.name, avg_grade = student.get_avg_grade(), image_url = student.image_url)
        print(text)          

def sort_list_by_grade():
    student_list = get_students_list()
    student_list.sort(key=lambda x: x.get_avg_grade(), reverse=False)
    for student in student_list:
        print(student.get_avg_grade())
            

def create_barchat():
    student_list = get_students_list()
    for student in student_list:
        plt.bar([student.name],[student.get_avg_grade()],width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')


def create_barchat_study_progression():
    student_list = get_students_list()
    progression_secruity = 0
    students_secruity = 0
    progression_typescript = 0
    students_typescript = 0
    progression_kotlin = 0
    students_kotlin = 0
    for student in student_list:
        for course in student.data_sheet.courses:
            if course.name == "Secruity":
                progression_secruity += student.get_progression()
                students_secruity += 1
            if course.name == "Typescript":
                progression_typescript += student.get_progression()
                students_typescript += 1
            if course.name == "Kotlin":
                progression_kotlin += student.get_progression()
                students_kotlin += 1

    plt.bar([progression_secruity ],["Secruity: " + str(students_secruity)],width=0.5, align='center')
    plt.bar([ progression_typescript],["Typescript: " + str(students_typescript)],width=0.5, align='center')
    plt.bar([progression_kotlin],["Kotlin: " + str(students_kotlin)],width=0.5, align='center')
    plt.xticks(rotation=45, horizontalalignment='right',fontweight='light',)





course = Course("hej","s", "sss", "222", 10)
data_sheet = DataSheet([course])
student = Student("hej", "sss", data_sheet, "sasdsa")
