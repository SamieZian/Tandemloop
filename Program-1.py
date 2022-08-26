#Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

def calculator(ls,opr):
    a = ls[0]
    b = ls[1]

    if opr == "add":
        print("Addition is",a+b)

    if opr == "sub":
        print("Substraction is",a-b)

    if opr == "div":
        print("Division is",a//b)

    if opr == "mul":
        print("Addition is",a*b)

    if opr == "mod":
        print("Addition is",a%b)



val = list(map(int,input().split()))
opr = input()

#calling a calulator operation
calculator(val,opr)
