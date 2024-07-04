#pattern 10 program
num = 5
for i in range(1,num+1):
    for j in range(1,i+1):
        if i % 2 == 0:
            print('#',end=" ")
        else:
            print('*', end=" ")
    print()

#pattern 11 program
num = 5
for i in range(1,num+1):
    for j in range(1,i+1):
        if i % 2 == 0:
            print(i, end=" ")
        else:
            print('*', end=" ")
    print()

#Output
* 
# # 
* * * 
# # # # 
* * * * * 

* 
2 2 
* * * 
4 4 4 4 
* * * * * 
