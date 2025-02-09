marks=int(input("marks:"))
if(marks>=94):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
else:
    grade="C"
print("grade of the student",grade)


age=int(input("age"))
if(age>=18):
    if(age>=80):
        print("canot drive")  #nesting 
    else:
        print("can drive")
else:
        print("NO")

number=int(input("number:"))   # even or odd
rem=number%2
if(rem==0):
    print("even")
else:
    print("odd")

a=4
b=5
c=3
if(a>b and a>c):          #greatest among all
    print("a is greatest")
elif(b>c and b>a):
    print(" bis greatest")
else:
    print("c is greatest")


num1=int(input("num1"))
if(num1%7==0):
        print("Multiple of 7")  #multiple of 7 
else:
        print("not ")

