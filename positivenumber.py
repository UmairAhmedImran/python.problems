number = int(input("Enter a positive numbeer to sum: "))
sum = 0
while(number > 0):
    sum += number
    print("\n---------------------------")
    number = int(input("Enter a positive numbeer to sum: "))
    
print(f"\nThe total sum of all numbers is {sum}")
