fee = 4500
for i in range(1,4):
    fee = fee + fee * 0.02
    print("---------------------------")
    print(f"fees after {i} year is {fee}")
    print("---------------------------\n")