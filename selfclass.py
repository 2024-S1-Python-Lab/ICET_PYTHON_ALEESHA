class Student:
    def get(self):
        self.rlno=int(input("enter roll number"))
        self.name=input("enter name:")
        self.totalmark=float(input("enter totalmark"))
    def disp(self):
            print("\nstudent details:")

            print(f"roll number:{self.rlno}")
            print(f"name:{self.name}")
            print(f"totalmark:{self.totalmark}")

stud1=Student()
stud1.get()
stud1.disp()

            
        
