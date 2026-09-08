Mobile_list=["iphone" , 128 , "white colour"]
print(Mobile_list)
print(type(Mobile_list))
print(len(Mobile_list))
for x in Mobile_list:
    print(x)

Mobile_list.append("100 bh")
print(Mobile_list)

Mobile_list.remove(128)
print(Mobile_list)

Mobile_list.pop(1)
print(Mobile_list)

Mobile_list.insert(1 ,"white colour")
print(Mobile_list)