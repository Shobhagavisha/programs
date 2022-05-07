my_list=[1,2,3,4, [5,6,7,8],[3,77,88],11,22,0.33]
def list1(my_list):

    for i in my_list:
        if type(i)==list:
            print(i)
list1(my_list)        