# 1

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))

list = [a,b,c,d]
list = sorted(list)
print(list[3])

# or 1
# if (a>b | c>d):
#     if (a>c):
#         print("a is grater",a)
#     else:
#         print("c is grater",c)
# elif(b>d):
#     print("b is grater",b)
# else:
#     print("c is grater", c)

# 0r 1
if a > b and a > c and a > d:
    print("a is greater", a)
elif b > c and b > d:
    print("b is greater", b)
elif c > d:
    print("c is greater", c)
else:
    print("d is greater", d)

