class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        avgnum = sum(self.scores) / len(self.scores)
        grade = "T"
        if avgnum >= 90 and avgnum <= 100:
            grade = "O"
        elif avgnum >= 80 and avgnum < 90:
            grade = "E"
        elif avgnum >= 70 and avgnum < 80:
            grade = "A"
        elif avgnum >= 55 and avgnum < 70:
            grade = "P"
        elif avgnum >= 40 and avgnum < 55:
            grade = "D"
        else:
            grade = "T"
        return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
