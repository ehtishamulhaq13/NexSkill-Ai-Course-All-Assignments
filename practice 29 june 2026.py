MobileName=input("Kindly enter mobile name:")   # enter name 
print(MobileName)
print(type(MobileName))
print(len(MobileName))
for x in MobileName:
    print(x)
# My first code ends here   

MobilePrice=float(input("Kindly Enter Mobile Price:"))
print(MobilePrice)

print(type(MobilePrice))
if MobilePrice > 5:
    print("greater 5")
elif MobilePrice < 5:
    print("less then 5")
elif MobilePrice < 3:
    print("Less then 3")       
else:
    print("What Ever")
    
   
