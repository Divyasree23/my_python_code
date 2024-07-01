#pattern matching printing rows in step wise
#pattern-1
num = 5
for i in range(1,num+1):  #i = 5
    for j in range(1,i+1): #i =5, j = 1,2,3,4,5
        print(i,end=" ")
    print( )

#pattern-2
for i in range(1,num+1):  #i = 5
    for j in range(1,i+1): #i =5, j = 1,2,3,4,5
        print(j,end=" ")
    print( )

#pattern-3
for i in range(1,num+1):  #i = 5
    for j in range(1,i+1): #i =5, j = 1,2,3,4,5
        print('*',end=" ")
    print( )
