firstname = input("Adınızı Giriniz: ")
lastname = input("Soyadınız Giriniz: ")
age = int (input("Yaşınızı Giriniz: "))
year = int (input("Doğum Yılınızı Giriniz: "))

userinfo =[]

userinfo.append(firstname)
userinfo.append(lastname)
userinfo.append(age)
userinfo.append(year)

#print (userinfo)
for i in userinfo:
    print(i)

if age < 18:
    print("You can't go out because it's too dangerous")  
else:
    print("You can go out to the sreet")  
