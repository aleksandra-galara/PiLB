a=float(input("Type in a:"))
b=float(input("Type in b:"))
c=float(input("Type in c:"))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b-delta**(1/2))/(2*a)
    x2 = (-b+delta**(1/2))/(2*a)
    print("x1 = {} \nx2 = {}".format(x1,x2))
elif delta==0:
    x1 = (-b)/(2*a)
    print("x1 = {}".format(x1))
else:
    print("Delta is lower than 0. No equantion root. ")
