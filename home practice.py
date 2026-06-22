# string variable

strvar = str("hello world - Ehti")
print(type(strvar))

strvar2 = "hello world - Ehti"
print(type(strvar2))

# int variable 

intvar = int(1305)
print(type(intvar))

intvar2 = 1305
print(type(intvar2))

# addition 
a=10
b=2

a+b
print("a+b=" , a+b)

# modulus
a%b
print("a%b=" , a%b)

# Exponent
a**b 
print("a**b=", a**b)

# floor division
a//b
print("a//b=" , a//b)

#greater then operater
print("b>a" , b>a)

# less then or equal operator
print("a<=b" , a<=b)

# and or not operator
print((a!=b) or (a>b))

# assignments operations
a=a+5
a+=20
print("a+=20:" ,a)

b=b+20
b-=10
print("b-=10:", b)

a//=3
print("a//=3:" , a)


# string operations
text=("call_ehti")
print("/nConverted String:")
print(text.upper())

print(text.swapcase())
print(text.title())

# for loop
for i in "call_ehti":
    print(i)

# sub string
st ="call_ehti"
print(st[2:6:1])
print(st[4::1])






