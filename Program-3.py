#With a single integer as the input, generate the following until a = x [series of numbers as shown in the below examples]


a = int(input())
if a % 2 == 0:
    a -=1
count = 1
while a > 0:
    print(count,end=" ")
    count += 2
    a -= 1
