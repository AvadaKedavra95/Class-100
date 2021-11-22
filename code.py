class Student(object):
    def __init__(self,name,age,gender,level,grades=None):
        self.name=name
        self.age=age
        self.gender=gender
        self.level=level
        self.grades=grades or {}
    def setGrade(self,course,grade):
        self.grades[course]=grade
    def getGrade(self,course):
        return self.grades[course]
    def getGPA(self):
        return sum(self.grades.values()/len(self.grades))


st1=Student("Jon",14,"male",9,{"math":33})
print(st1.getGPA())

