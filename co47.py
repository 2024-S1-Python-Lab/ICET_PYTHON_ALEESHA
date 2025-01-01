class Time:
  def __init__(self): #Initialize the Time object
     self.__hours = int(input("Enter the hours: "))
     self.__minutes = int(input("Enter the minutes: "))
     self.__seconds = int(input("Enter the seconds: "))
  def __add__(self, other): #Overload the '+' operator to add two Time objects
     total_seconds = self.__seconds + other.__seconds
     total_minutes = self.__minutes + other.__minutes + (total_seconds // 60)
     total_hours = self.__hours + other.__hours + (total_minutes // 60)
# Keep time within a 24-hour format
     seconds = total_seconds % 60
     minutes = total_minutes % 60
     hours = total_hours % 24
     return f"{hours}:{minutes}:{seconds}"
# Create two Time objects
print("Enter details for Time 1:")
t1 = Time()
print("\nEnter details for Time 2:")
t2 = Time()
result = t1 + t2 # Add the two times using the overloaded '+' operator
print("Sum of the two times:", result)
  
