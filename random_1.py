import random

def numbers(N,A,B):
    even = 0
    odd = 0
    for i in range(1, N+1):
        num = random.randrange(A,B)
        print(num)
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print(f"Number of even value is {even} and odd value is {odd}")

N = int(input("Enter the number of random values you need: "))
A = int(input("Enter the initial number: "))
B = int(input("Enter the final number: "))

numbers(N,A,B)

