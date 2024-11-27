from assets import studentList
from model.student import Student

newStudent = Student('','','','','')
newStudent.accept()

newStudent.enterGradesForAll()

def deleteStudent():
    if len(studentList) >= 1:
        newStudent.delete()

deleteStudent()

def updateStudent():
    newStudent.update_idNum()

updateStudent()

newStudent.displayAllStudents()
