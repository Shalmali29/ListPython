list=[]
n=int(input("enter number of elements in list:"))
print("enter the elements:")
for i in range (0,n):
    element=int(input())
    list.append(element)
print("the list is :\n")
print(list)
print("the positive numbers present in the list are:")
for i in range(0,n):
    if(list[i]>0):
        print(list[i])
    
