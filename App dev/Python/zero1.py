#Bing En
_ = input("Choose a number to divide: ")
try:
    print(*["You suck" for _ in range(int(10//float(_)))], sep="\n")
except ValueError:
    print("It's not even a number you dumbfuck")
except ZeroDivisionError:
    print("Quit dividing by zero fucking idiot")

#Leroy
