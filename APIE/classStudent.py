class Student:
    college_name = "NiT"

    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def welcome():
        print("Welcome ",s1.name,"! ","\nYour marks is ",s1.get_marks(),"\nWelcome ",s2.name,"! ","\nYour marks is ",s2.get_marks(),sep="")

    def get_marks(self):
        return self.marks
    
s1 = Student("Shubham",85)
s2 = Student("Vishal",90)
Student.welcome()
#print("Your marks is",s1.get_marks())
#print("Your marks is",s2.get_marks())