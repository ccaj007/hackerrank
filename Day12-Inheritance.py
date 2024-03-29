class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores


#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):

        avg_grade = sum(self.scores) / len(self.scores)

        if (90 <= avg_grade <= 100):
            return "O"
        if (80 <= avg_grade < 90):
            return "E"
        if (70 <= avg_grade < 80):
            return "A"
        if (55 <= avg_grade < 70):
            return "P"
        if (40 <= avg_grade < 55):
            return "D"
        if (avg_grade < 40):
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNUmber = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNUmber, scores)
s.printPerson()
print("Grade:", s.calculate())

'''
sample input:
Heraldo Memelli 8135627
100 80
'''