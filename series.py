n=int(input("Enter the number of terms: "))
s=1
for i in range(1,n+1):
    s=s+(1/2**i)
print("\n---------------------------")
print(f"The sum of series is {s}")
print("---------------------------")