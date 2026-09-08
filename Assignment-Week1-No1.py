# Question:1
# Write a  python program that converts a temperature from Celsius to Fahrenheit.
# (Formula: Fahrenheit = (Celsius * 9/5) + 32)  


celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)





# Question 2: 
# Calculate Area of a Rectangle 

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = length * width

print("Area of the rectangle:", area)






# Question 3: 
# Calculate Compound Interest Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time 

P = float(input("Enter Principal Amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time in Years (T): "))

CI = P * (1 + R/100) ** T - P

print("Compound Interest =", CI)





# Question 4: 
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter. 


length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

perimeter = 2 * (length + width)

print("Perimeter of the rectangle:", perimeter)





# Question 5: 
# Average of Three Numbers - Input three numbers and print their average. 


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)







# Question 6: 
# Square and Cube of a Number - Ask the user for a number and display its square and cube. 


number = float(input("Enter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)







# Question 7: 
# Distribute Items Equally - You have n candies and k students. 
# Write a program to find: 
# how many candies each student gets how many are left 


candies = int(input("Enter the number of candies: "))
students = int(input("Enter the number of students: "))

each_student_gets = candies // students
candies_left = candies % students

print("Each student gets:", each_student_gets)
print("Candies left:", candies_left)









# left Question 8: 
# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
 
#Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss 


cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)

else:
    print("No Profit No Loss")








# Question 9: 
# Total Marks and Percentage 
# Input marks of 5 subjects. Print: 
# •	Total marks 
# •	Percentage 
# •	Average



sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks =", total)
print("Percentage =", percentage, "%")
print("Average =", average)










# Question 10: 
# Salary Calculator 
# Input basic salary. Calculate: 
# •	HRA = 20% of basic 
# •	DA = 15% of basic 
# •	Total Salary = Basic + HRA + DA 


basic_salary = float(input("Enter Basic Salary: "))

HRA = basic_salary * 20 / 100
DA = basic_salary * 15 / 100

total_salary = basic_salary + HRA + DA

print("HRA =", HRA)
print("DA =", DA)
print("Total Salary =", total_salary)







# Question 11: 
# Age in Months and Days 
# Input your age in years. Calculate and print age in: 
# •	Months 
# •	Days (approximate)

age_years = int(input("Enter your age in years: "))

months = age_years * 12
days = age_years * 365   # Approximate days

print("Age in Months =", months)
print("Age in Days =", days)








# Question 12: 
# Currency Converter (USD to PKR) 
# Input amount in USD. Convert using a fixed exchange rate. 


usd = float(input("Enter amount in USD: "))

exchange_rate = 280  

pkr = usd * exchange_rate

print("Amount in PKR =", pkr)








# Question 13:
# Sum of First N Natural Numbers 
# Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2 



n = int(input("Enter a number: "))

sum_n = n * (n + 1) / 2

print("Sum of first", n, "natural numbers =", sum_n)










 
# Question 14: 
# Percentage of Correct Answers 
# Input total questions and correct answers, and calculate the percentage score. 


total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

percentage = (correct_answers / total_questions) * 100

print("Percentage Score =", percentage, "%")








# Question 15: 
# Speed, Distance, and Time 
# Input distance and time, and calculate speed. 


distance = float(input("Enter distance: "))
time = float(input("Enter time: "))

speed = distance / time

print("Speed =", speed)









# Question 16: 
# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2) 


weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

BMI = weight / (height ** 2)

print("BMI =", BMI)








# Question 17:
# Convert Minutes to Hours and Minutes 

minutes = int(input("Enter total minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours =", hours)
print("Minutes =", remaining_minutes)





