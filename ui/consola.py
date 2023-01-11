from Service.StudentService import StudentService

class Consola:
    def __init__(self, studentService: StudentService):
        self.__studentService = studentService

    def adaugaStudent(self):
        try:
            studentID = input("Dati ID-ul studentului: ")
            nume = input("Dati numele studentului: ")
            grup = input("Dati grupul studentului: ")
            self.__studentService.adauga(studentID, nume, grup)
        except KeyError as e:
            print(e)

    def modificaStudent(self):
        try:
            studentID = input("Dati ID-ul studentului care sa fie modificat: ")
            numeNou = input("Dati noul nume al studentului: ")
            grupNou = input("Dati noul grup al studentului: ")
            self.__studentService.modifica(studentID, numeNou, grupNou)
        except KeyError as e:
            print(e)

    def stergeStudent(self):
        try:
            studentID = input("Dati ID-ul studentului care sa fie sters: ")
            self.__studentService.sterge(studentID)
        except KeyError as e:
            print(e)

    def afiseaza(self,entitati):
        for entitate in entitati:
            print(entitate)
    def printMeniu(self):
        print("1. Adauga student")
        print("2. Modifica student")
        print("3. Sterge student")
        print("a. Afiseaza toti studentii")
        print("x. Iesire")

    def meniu(self):
        while True:
            self.printMeniu()
            tasta = input("Dati optiunea: ")
            if tasta == "1":
                self.adaugaStudent()
            elif tasta == "2":
                self.modificaStudent()
            elif tasta == "3":
                self.stergeStudent()
            elif tasta == "a":
                self.afiseaza(self.__studentService.getALLStudenti())
            elif tasta == "x":
                break
            else:
                print("Optiune grestia")