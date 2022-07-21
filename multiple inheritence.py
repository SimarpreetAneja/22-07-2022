class student:
    def student(self):
        print("student name")
class mother:
    def mother(self):
        print("mother name")
class father(student,mother):
    def father(self):
        print("father name")
ob=father()
ob.father()
ob.mother()
ob.student()
