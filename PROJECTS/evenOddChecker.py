#Even or odd checker

try:
    num = int(input("Input number:"))

    if (num%2 == 0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

except ValueError:
    print("Input valid number!")
