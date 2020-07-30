# FAULTY CALCULATOR : EXERSICE 2:: # THIS CALCULATOR ONLY SUPPORTS OPERATORS LIKE +, -, / AND *.
A = int(input("ENTER A FIRST NO.\n : "))
B = input("ENTER THE OPERATOR YOU WANT TO USE :\n : ")
C = int(input("ENTER ANOTHER NO.\n : "))
if A == 45 and B == "*" and C == 3:
    print("45 * 3 = 555")
elif A == 56 and B == "+" and C == 9:
    print("56 + 9 = 77")
elif A == 56 and B == "/" and C == 6:
    print("56 + 6 = 4")
elif B == "+":
    print(A, B, C, "=", A + C)
elif B == '-':
    print(A, B, C, "=", A - C)
elif B == '*':
    print(A, B, C, "=", A * C)
elif B == '/':
    print(A, B, C, "=", A / C)
else:
    print("calculator mar gaya RIP :(")
