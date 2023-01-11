class Studentrepository:
    def __init__(self):
        self.__studenti = {}

    def getAll(self):
        """
        returneaza lista de studenti
        :return: o lista de obiecte de tipul studenti
        """
        # daca am scrie return self.__studenti, am returna un dictionar
        # iar layerele "de mai sus" au nevoie de o lista( ex. cand afisam studenti,
        # este mai citibil daca afisam o lista vs un dictionar)
        return list(self.__studenti.values())

    def getByID(self, studentID):
        """
        returneaza studentul cu id-ul dat
        :param studentID: string
        :return: un obiect de tipul student, daca exista unul cu id-ul dat,altfel None
        """
        if studentID in self.__studenti:
            return self.__studenti[studentID]
        return None
        #return self.__studenti[studentID, None]

    def adauga(self, student):
        """
        adauga un student in dictionar
        :param student: obiect de tipul Student
        :return:
        """
        if self.getByID(student.getStudentID()) is not None:
            raise KeyError("Exista deja un student cu ID-ul dat.")
        self.__studenti[student.getStudentID()] = student

    def modifica(self, studentNou):
        """
        modifica un angajat dupa id
        :param studentNou: obiect de tipul Student
        :return:
        """
        if self.getByID(studentNou.getStudentID()) is None:
            raise KeyError("Nu exitsa niciun student cu ID-ul dat!")
        self.__studenti[studentNou.getStudentID()] = studentNou

    def sterge(self, studentID):
        """
        sterge un angajat dupa id
        :param studentID: string
        :return:
        """
        if self.getByID(studentID) is None:
            raise KeyError("Nu exista niciun student cu ID-ul dat!")
        self.__studenti.pop(studentID)
