from Domeniu.Studenti import Student
from Repository.StudentRepository import Studentrepository


class StudentService:
    def __init__(self, studentRepository: Studentrepository):
        self.__studentRepository = studentRepository

    def getALLStudenti(self):
        """
        returneaza lista de studenti
        :return: o lista de obiecte de tipul Student
        """
        return self.__studentRepository.getAll()

    def adauga (self, studentID, nume, grup):
        """
        adauga un student
        :param studentID: string
        :param nume: string
        :param grup:
        :return:
        """
        student = Student(studentID, nume, grup)
        self.__studentRepository.adauga(student)

    def modifica(self, studentID, numeNou, grupNou):
        """
        modifica un student dupa id
        :param studentID: string
        :param numeNou: string
        :param grupNou: int
        :return:
        """
        studentNou = Student(studentID, numeNou, grupNou)
        self.__studentRepository.modifica(studentNou)

    def sterge(self, studentID):
        """
        sterge un student dupa ID
        :param studentID: string
        :return: 
        """
        self.__studentRepository.sterge(studentID)
