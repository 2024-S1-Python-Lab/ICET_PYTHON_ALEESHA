class Student:
    def get(self,rlno,name,totalmark):
        self.rlno=rlno
        self.name=name
        self.totalmark=totalmark
        
    def disp(self):
            print(f"Roll number:{self.rlno}")
            print(f"Name:{self.name}")
            print(f"Total mark:{self.totalmark}")
stud1=Student()
stud1.get(101,"alice",85)
stud1.disp()
























                     
