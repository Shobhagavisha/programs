from socket import EAI_AGAIN


ch=input("enter a character")
ascii=ord(ch)
def char(ch):
   
    if (ascii>=65 and ascii<=90):
        print("uppercase")
        
    elif(ascii>=90 and ascii<=127):
        print("lower")    

char(ch)


#string program

num=input("enter a string")
for each_item in num:
    
    if(each_item=='a' or each_item=='A'):
    
        print('$')

#change character

def change_char(str1):
    char=str1[0]
    str1=str1.replace(char,'#')
    str1=str1+char[1:]
    return str1
print(change_char('sgfhfsffsss'))


    


  
