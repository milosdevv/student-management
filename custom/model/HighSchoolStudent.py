from model.Student import Student, studentList

class HighSchoolStudent(Student):
    def __init__(self, firstName, lastName, idNum, subject, grade, faculty, schoolName):
        super().__init__(firstName, lastName, idNum, subject, faculty, grade)
        self.schoolName = schoolName
    
    def display(self):
        super().display()
        print(f'School name: {self.schoolName}')
    
    def accept(self):
       while True:
           
        accSchoolStudent = input('Da li zelite da prijavite srednjoskolca? (y/n) ')
        
        if accSchoolStudent.lower() == 'y':
            while True:
                firstNameInput = input('Ime: ').strip()
                lastNameInput = input('Prezime: ').strip()
                if firstNameInput == '' or lastNameInput == '':
                    print('Greska! Ime i prezime ne smeju biti prazni. Molimo pokusajte ponovo.')
                    continue
                if firstNameInput[0].isdigit() or lastNameInput[0].isdigit():
                    print('Greska! Ime ne sme poceti sa brojem! molimo pokusajte ponovo')
                    continue
                else:
                    break
            while True:
                    rollNumInput = input('Molim dodelite vas ID broj: ')
                    if rollNumInput.isdigit():
                        rollNumInput = int(rollNumInput)
                        break
                    else:
                        print('Greska: ID broj mora biti broj. Molimo pokusajte ponovo')
            while True:
                subjectInput = input('Predmet za ocenu: ').strip()
                facultyInput = ''
                schoolNameInput = input('Naziv ustanove: ').strip()
                if subjectInput == '' or schoolNameInput == '':
                    print('Greska! Predmet i naziv ustanove ne smeju biti prazni. Molimo pokusajte ponovo.')
                    continue
                if subjectInput[0].isdigit() or schoolNameInput[0].isdigit():
                        print('Greska! molimo pokusajte ponovo')
                        continue
                else:
                    break
            gradeInput = ''

            new_highschoolStudent = HighSchoolStudent(
            firstNameInput,lastNameInput,rollNumInput,subjectInput,gradeInput,facultyInput,schoolNameInput
            )

            studentList.append(new_highschoolStudent)

            print(
                    f'Srednjoškolac {firstNameInput} {lastNameInput} sa rednim brojem [{rollNumInput}] '
                    f'je uspešno prijavljen za predmet {subjectInput} iz škole {schoolNameInput}'
            )

            new_highschoolStudent.display()
        elif accSchoolStudent == 'n':
            print('Prijava srednjoskolca je zavrsena!')
            break  
        else:
            print("Molimo unesite 'y' ili 'n'.")

    def displayAllStudents(self):
        return super().displayAllStudents()
        

