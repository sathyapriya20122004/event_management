a=int(input("enter the number:"))
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")    



age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


num=int(input("enter a number:")) 
r=0
if num>0:
    d=num%10
    r=r*10
    r+=d
    num//=10
print("reversed number is:",r)

n=int(input("enter the number:"))
count=0
if n==0:
    count=1
else:
    while n!=0:
        n//=10
        count+=1
print("number ofdigits:",count)
    

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print("")

import math 
a = int(input("enter the number: "))
print("factorial of ",a,"is",math.factorial(a))


i = str(input("Enter a string: "))

nor= i

rev = nor[::-1]

if nor == rev:
    print(f"'{i}' is a palindrome.")
else:
    print(f"'{i}' is not a palindrome.")



li=[1,2,"three",7]
print(li)
li.append(4)
print(li)
li.insert(2,7)
print(li)


tup=(10,5,20)
t=tuple("string")
print(tup[1])
print("value in tup[-2]=",t[0])
print("value in tup[-3]=",tup[-3])


num=5
fac=1
for i in range(1,num+1):
    fac*=i
print(fac)


class stud:
    def __init__(self,name,roll_no,age,grade):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.grade=grade
    def __str__(self):
        return f"{self.name}{self.roll_no}{self.age}{self.grade}"
p1=stud("vijay",1848,20,"A")
print(p1)
print( "name =",p1.name)
print("roll no =", p1.roll_no)
print("age =",p1.age)
print("grade =",p1.grade)
                                                                                              