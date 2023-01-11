from Repository.StudentRepository import Studentrepository
from Service.StudentService import StudentService
from ui.consola import Consola


def main():
    studentRepository = Studentrepository()
    studentService = StudentService(studentRepository)
    consola = Consola(studentService)

    consola.meniu()

main()