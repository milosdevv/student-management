from model.Student import Student,studentList
from model.HighSchoolStudent import HighSchoolStudent

def createStudent(student_type):
    if student_type == 1:
        student = Student('', '', '', '', '', '')
    else:
        student = HighSchoolStudent('', '', '', '', '', '', '')
    
    student.accept()
    student.enterGradesForAll()
    return student

def handleStudentActions(student):
    if len(studentList) == 0:
        print('Lista studenata je prazna. Molim Vas da unesete studente!')
        return
    student.delete()
    student.update_idNum()
    student.displayAllStudents()

def chooseStudent():
    while True:
        try:
            question = int(input('Student/srednjoskolac? (1/2) '))
            if question not in [1, 2]:
                print("Molimo unesite 1 za studenta ili 2 za srednjoskolca.")
                continue
            break
        except ValueError:
            print("Pogrešan unos, molimo unesite broj 1 ili 2.")
    
    student = createStudent(question)
    handleStudentActions(student)

chooseStudent()
