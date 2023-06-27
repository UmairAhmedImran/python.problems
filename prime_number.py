import math
def prime_function(x):
    flag = 1
    for i in range(2,int(math.sqrt(x))+1): # range[2,sqrt(num)]
        if(x%i==0):
            flag=0
            print("\n---------------------------")
            print(f"{x} is not a Prime number")
            print("---------------------------")
            break
        else:
            continue
    if(flag==1):
        print("\n---------------------------")
        print(f"{x} is a Prime number")
        print("---------------------------")
        return flag

num = int(input("Enter the number: "))
prime_function(num)

