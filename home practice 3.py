print("==Student Information System==")
while True:
  Name = input("Enter Your Name:")
  Roll_no = input("Enter Your Roll_no:")

  Subject1 = float(input("Enter Marks For Subject 1:"))
  Subject2 = float(input("Enter Marks For Subject 2:"))
  Subject3 = float(input("Enter Marks For Subject 3:"))
  Total_Marks =Subject1+Subject2+Subject3
  Average=Total_Marks/3

  if Average >=80:
    Grade = "A"
  elif Average>=70:
    Grade = "B"
  elif Average>=60:
    Grade = "C"
  elif Average>=50:
    Grade = "D"
  else:
    ("Fail")     

  print("/n==student Result")
  print("Name:",Name)
  print("Roll_no:",Roll_no)      
  print("Total_Marks:",Total_Marks)
  print("Average:",round(Average,2))
  print("Grade:",Grade)
  

  choice=("\nDo you want to enter another student record? (yes/no):")
  if choice.lower() !="yes":
    print("\nThank you for using Student Grade Management System!")
    break












