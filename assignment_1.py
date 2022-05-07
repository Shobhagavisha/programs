#nested list progra


my_list=[1,2,3,4, [5,6,7,8],[3,77,88],11,22,0.33]
def list1(my_list):

    for i in my_list:
        if type(i)==list:
            print(i)
list1(my_list)        

# dictionary  program

my_dict={'a':1,'b':'rishika','c':4,'d':"harsha"}
#print(my_dict.get('d'))
print(my_dict)
final_dict={}
key = input("please enter the key, that you want to pe printed\n")
req_word = my_dict.get(key)
for i in req_word:
#for i in (my_dict.get('d')):
    if i in final_dict:
        final_dict[i]=final_dict[i]+1
    else:
        final_dict[i]=1
print(final_dict)

# sample_matrix transpose program

sample_matrix=[[2,3],[3,4],[5,6]]
for m in sample_matrix:
    print(m)
transpose=[[sample_matrix[j][i] for j  in range(len(sample_matrix))] for i in range(len(sample_matrix[0]))]
print("transpose matrix is:")
for t in transpose:
    print(t)   


