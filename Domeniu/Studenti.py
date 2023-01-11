class Student:
    def __init__(self, studentID, nume, grup):
        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup

    def getStudentID(self):
        return self.__studentID

    def getNume(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def setStudentID(self, studentID):
        self.__studentID = studentID

    def setNume(self, nume):
        self.__nume = nume

    def setGrup(self, grup):
        self.__grup= grup

    def __str__(self):
        return f"id: {self.__studentID}, nume: {self.__nume}, grup: {self.__grup}"


