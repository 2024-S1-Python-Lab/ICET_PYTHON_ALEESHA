class Bank:
    def __init__(self,accNo,name,accType,balance=0):
        self.acc=accNo
        self.na=name
        self.accType=accType
        self.bal=balance
    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            print(f"deposit successful!new balance:{self.bal}")
        else:
            print("inalid deposit amount.please enter a positive value.")        
                
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.bal:
                self.bal-=amount
                print(f"withdrawal successful! new balance:{self.bal}")
            else:
                print("insufficient balance.")
        else:
            print("invalid withdrawal amount.please enter a positive value.")
    def display(self):
        
        print(f"\n account number:{self.acc}\n account holder name:{self.na}")
        print(f"account Type:{self.accType}\n balance:{self.bal}")
        print("\n***Menu ***")
        print("1.deposit\n2.withdraw\n3.display\n4.exit")
                    
b1=Bank(1002,"nidhi","savings",0)
b1.display()
while True:
    choice=int(input("\nenter your choice(1-4):"))
    if choice==1:
        d=int(input("enter amount to be deposited:"))
        b1.deposit(d)
    elif choice==2:
        w=int(input("enter amount to withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("exiting..thank you!")
        break
    else:
        print("enter a valid choice")
                                 
                                      
                                     
                                       
                                            
                                            
                                           
                                                  
                                                  
                                                   

      
                    
        
                
      
        
         
    
        
           
            
            
             
                     
                    
                         
                        
                             
                              
                       
                                 
                                  
                            
                                     
                            
                                           
                                          

                
                                       
