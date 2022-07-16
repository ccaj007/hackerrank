# https://www.hackerrank.com/challenges/30-class-vs-instance/problem?isFullScreen=true

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print('you enter negative number, age will be 0')
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (self.age < 13):
            print('you are a child')
        elif ( 13 <= self.age <= 18):
            print('you are a teenager')
        else:
            print('you are old')

    def yearPasses(self):
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


