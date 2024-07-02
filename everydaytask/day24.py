#pattern 7 program
num = 6
for i in range(1,num):
    for j in range(i,num):
        print(i,end=" ") #f'{i,j}'
    print()

#pattern 8 program
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(j,end=" ") #f'{j,i}',end=" "
    print()

#pattern 9 program
for i in range(1,num+1):
    for j in range(i,num):
        print('*',end=" ")
    print()

Output
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 


* * * * * 
* * * * 
* * * 
* * 
* 

