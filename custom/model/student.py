studentList = []
class Student():

    def __init__(self,firstName,lastName,idNum,subject,grade,faculty):

        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.subject = subject
        self.grade = grade
        self.faculty = faculty

    def display(self):
        print('\n')
        print(f'Ime i prezime: {self.firstName} {self.lastName}')
        print(f'ID: {self.idNum}')
        print(f'Predmet: {self.subject}')
        print(f'Fakultet {self.faculty}')
    # Prijava studenta
    def accept(self):
        while True:
            accStudent = input('Da li zelite da prijavite studenta? (y/n) ').strip().lower()

            if accStudent == 'y':
                # Accept student information
                while True:
                    firstNameInput = input('Ime: ')
                    lastNameInput = input('Prezime: ')
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
                    subjectInput = input('Predmet za ocenu: ')
                    facultyInput = input('Naziv ustanove: ')
                    if subjectInput[0].isdigit() or facultyInput[0].isdigit():
                        print('Greska! molimo pokusajte ponovo')
                        continue
                    else:
                        break

                gradeInput = ''  # Initial grade is empty
                new_student = Student(firstNameInput, lastNameInput, rollNumInput, subjectInput, gradeInput, facultyInput)
                studentList.append(new_student)
                new_student.display()
                print(f'Student {firstNameInput} {lastNameInput} {rollNumInput} je uspesno prijavljen sa ocenom {gradeInput} za predmet {subjectInput}. Fakultet studenta je: {facultyInput}')
            elif accStudent == 'n':
                print('Prijava studenata je završena.')
                break
            else:
                print('Morate uneti "y" ili "n". Pokušajte ponovo.')
    #Unosenje ocene studenta
    def enterGradesForAll(self):
        while True:
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
                            print("Molimo unesite validnu ocenu.")
                        continue
                    elif confirmGrade.lower() == 'n':
                        continue
                break
            else:
                print("Lista studenata je prazna.")
                break

    # Brisanje studenta iz liste
    def delete(self):
        while True:
            if len(studentList) == 0:
                print('Lista studenata je prazna. Molim Vas da unesete studente!')
                return
            confirmdel = input('Da li zelite da obrisete studenta? (y/n): ')
            if confirmdel.lower() == 'y':
                while True:
                    try:
                        delStudent = input('Molimo vas da unesete njegov redni broj: ')
                        if delStudent.strip() == '':
                            print("Unos ne može biti prazan. Molimo unesite redni broj.")
                            continue
                        delStudent = int(delStudent)
                        break
                    except ValueError:
                        print("Molimo unesite validan broj za redni broj.")

                for student in studentList:

                    if student.idNum == delStudent:
                        studentList.remove(student)
                        print(f'Student {student.firstName} {student.lastName} (Redni broj: {student.idNum}) je obrisan.')
                        print(f'Preostali studenti: {len(studentList)}')
                        break
            elif confirmdel.lower() == 'n':
                print('Brisanje studenata zavrseno')
                break
                
            else:
                print("Molimo unesite 'y' ili 'n' za odgovor.")
                continue
    
    # Update rednog broja studenta
    def update_idNum(self):
        while True:
            if len(studentList) >= 1:
                while True:
                    confirmUpdate = input('Da li zelite da azurirate studenta? (y/n): ').lower()
                    if confirmUpdate == 'y' or confirmUpdate == 'n':
                        break
                    else:
                        print("Molimo unesite 'y' ili 'n'.")

                if confirmUpdate.lower() == 'y':
                    current_id = int(input("Unesite trenutni redni broj studenta za azuriranje: "))
                    current_name = input('Unesite ime studenta za azuriranje: ')
                    current_lastName = input('Unesite prezime studenta za azuriranje: ')
                    current_faculty = input('Unesite naziv trenutnog fakulteta koji studirate: ')
                    student_found = False

                    for student in studentList:
                        if student.firstName == current_name and student.lastName == current_lastName and student.idNum == current_id and student.faculty == current_faculty:
                            student_found = True
                            
                            while True:
                                try:
                                    new_id = int(input(f'Unesite novi redni broj za studenta {student.firstName} {student.lastName}: '))
                                    break
                                except ValueError:
                                     print("Molimo unesite validan broj za novi redni broj.")
                            student.idNum = new_id
                            print(f'Redni broj studenta {student.firstName} {student.lastName} je uspešno promenjen na {new_id}.')

                            while True:
                                new_name = input('Unesite novo ime za studenta: ')
                                if new_name:
                                    break
                                else:
                                    print("Ime ne može biti prazno. Molimo unesite validno ime.")
                            while True:
                                new_lastName = input('Unesite novo prezime za studenta: ')
                                if new_lastName:
                                    break
                                else:
                                    print("Prezime ne može biti prazno. Molimo unesite validno ime.")
                            student.firstName = new_name
                            student.lastName = new_lastName
                            print(f'Novo ime studenta je {student.firstName} {student.lastName}.')

                            while True:
                                new_faculty = input('Naziv ustanove koji menjate: ').strip()
                                if new_faculty:
                                    break
                                else:
                                    print("Naziv fakulteta ne može biti prazan. Molimo unesite validan naziv fakulteta.")

                            student.faculty = new_faculty
                            print(f'Student {student.firstName} {student.lastName} sa rednim brojem {new_id} se prebacio na fakultet: {new_faculty}')
                            break

                    if not student_found:
                        print(f'Student sa ID brojem {current_id} nije pronadjen')
                else:
                    print('Azuriranje je zavrseno.')
                    break  
            else:
                print('Nemate dovoljno studenata za azuriranje.')
                break
    # Prikazivanje svih studenata u listi
    def displayAllStudents(self):
        input('Da li zelite da pogledate sve studente? (y/n) ')
        if len(studentList) > 0:
            print('Lista svih studenata')
            for student in studentList:

                student.display()
                print('\n')
        else:
            print('Lista studenata je prazna')