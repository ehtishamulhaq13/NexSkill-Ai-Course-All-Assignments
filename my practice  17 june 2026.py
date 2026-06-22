bookyear = 2022
bookprice = 44.5

result = (bookyear*bookprice)
print(result)
print(type(bookyear))
print(type(bookprice))
print(type(result))

if bookprice > 50:
    print("Positive number")
elif bookprice < 0:
    print("Negative number")
else:
    print("zero")         
 
print("this statment is always executed")
