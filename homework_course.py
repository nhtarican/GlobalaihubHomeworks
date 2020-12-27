student_name = 'nihat'
student_surname = 'arican'
lessons= {1:'ders1', 2:'ders2', 3:'ders3', 4:'ders4', 5:'ders5', 6:'ders6', 7:'ders7',8:'ders8', 9:'ders9', 'q':'Çıkış'}
count = 3


while True:

    if (count > 0):
        name = input("Lütfen Adınızı Giriniz: ")
        surname = input("Lütfen Soyadınızı Giriniz ")

        if  (name == student_name) and (surname==student_surname):
            print (f'Hoşgeldiniz {name  + surname}\n' )
            break
        elif (name != student_name) and (surname==student_surname):
             print ('Adınızı Yanlış Girdiniz Tekrar Deneyin!')     
        elif (name == student_name) and (surname!=student_surname):
             print ('Soyadınızı Yanlış Girdiniz Tekrar Deneyin!') 
        elif (name!=student_name) and (surname!=student_surname): 
            print('Adınızı ve Soyadınızı Yanlış Girdiniz Tekrar Deneyin!')     

        count  -=1
        
    else:
        print('3 Kere Yanlış Girdiğiniz. Lütfen Daha Sonra Tekrar Deneyiniz!')   
        break  

print('DERSLER \n' )     

def print_all_courses():
    for key, lesson in lessons.items():
            print("{} - {}".format(key, lesson))


print_all_courses()

    

    
