from assets import studentList

class Student():

    def __init__(self,firstName,lastName,idNum,subject,grade):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.subject = subject
        self.grade = grade

    def __str__(self):
    
        return f'{self.firstName} {self.lastName} (ID: {self.idNum}), Predmet: {self.sub1}'

    def display(self):
        print('\n')
        print(f'Ime i prezime: {self.firstName} {self.lastName}')
        print(f'ID: {self.idNum}')
        print(f'Predmet: {self.subject}')
    # Prijava studenta
    def accept(self):

        while True:

            accStudent = input('Da li zelite da prijavite studenta? (y/n) ')

            if accStudent.lower() == 'y':

                firstNameInput = input('Ime: ')
                lastNameInput = input('Prezime: ')
                
                while True:
                    
                    try:
                        rollNumInput = int(input('Molim dodelite vas ID broj: '))
                        break
                    except ValueError:
                        print('Greska: ID broj mora biti broj. Molimo pokusajte ponovo')

                subjectInput = input('Predmet za ocenu: ')
                gradeInput = ''

                new_student = Student(firstNameInput, lastNameInput, rollNumInput, subjectInput, gradeInput)
                studentList.append(new_student)
                
                print(f'Student {firstNameInput} {lastNameInput} {rollNumInput} je uspesno prijavljen sa ocenom {gradeInput} za predmet {subjectInput}')
                new_student.display()
            else:
                print('Prijava studenata je završena.')
                break
    #Unosenje ocene studenta
    def enterGradesForAll(self):
        if len(studentList) > 0:
            print("Unos zakljucnih ocena za sve studente:")
            for student in studentList:
                confirmGrade = input(f'Da li zelite da date zakljucnu ocenu studentu {student.firstName} {student.lastName} iz predmeta {student.subject}? (y/n): ')
                
                if confirmGrade.lower() == 'y':
                    try:
                        giveGrade = int(input(f'Izaberite ocenu za ucenika {student.firstName} {student.lastName} [1, 2, 3, 4, 5]: '))

                        if giveGrade < 1 or giveGrade > 5:
                            print('Nevazeca ocena. Unesite ocenu između 1 i 5.')
                        elif giveGrade <= 2:
                            print('Ovo je losa ocena')
                        elif giveGrade >= 3:
                            print('Dobra ocena')
                        student.grade = giveGrade

                    except ValueError:
                        print("Molimo unesite validnu brojčanu vrednost za ocenu.")
        else:
            print("Lista studenata je prazna.")

    # Brisanje studenta
    def delete(self):
        while True:
            if len(studentList) == 0:
                print('Lista studenata je prazna. Molim Vas da unesete studente!')
                return
            
            confirmdel = input('Da li zelite da obrisete studenta? (y/n): ')
            
            if confirmdel.lower() == 'y':
                delStudent = int(input('Molimo vas da unesete njegov ID broj: '))

                for student in studentList:

                    if student.idNum == delStudent:
                        studentList.remove(student)
                        print(f'Student {student.firstName} {student.lastName} (ID: {student.idNum}) je obrisan.')
                        print(f'Preostali studenti: {len(studentList)}')
                        break
            else:
                print('Brisanje studenata zavrseno')
                break
    
    # Update ID studenta
    def update_idNum(self):

        while True:

            if len(studentList) >= 1:
                confirmUpdate = input('Da li zelite da azurirate studenta? (y/n)')

                if confirmUpdate.lower() == 'y':
                    current_id = int(input("Unesite trenutni ID studenta za ažuriranje: "))
                    student_found = False

                    for student in studentList:

                        if student.idNum == current_id:
                            student_found = True
                            new_id = int(input(f'Unesite novi ID za studenta {student.firstName} {student.lastName}: '))
                            student.idNum = new_id
                            print(f'ID studenta {student.firstName} {student.lastName} je uspešno promenjen na {new_id}.')
                            break  

                    if not student_found:
                        print(f'Student sa ID brojem {current_id} nije pronadjen')

                else:
                    print('Azuriranje ID broja je zavrseno.')
                    break  

            else:
                print('Nemate dovoljno studenata za ažuriranje ID broja.')
                break
    # Prikazivanje svih studenata
    def displayAllStudents(self):

        input('Da li zelite da pogledate sve studente? (y/n) ')

        if len(studentList) > 0:

            print('\n')
            print('Lista svih studenata')
            print('\n')

            for student in studentList:

                student.display()
                print('\n')

        else:
            print('Lista studenata je prazna')