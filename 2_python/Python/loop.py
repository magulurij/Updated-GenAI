count=1
while count<=5:
    print("hello")
    count+=1
    print(count)         #while
#here i,count is iterators and inside loop happening thing is called iteration.

    i=1
    while i<=5:
        print("hello hero")
        i+=1
        print(i)
    

i=1
while i<=6:
    print(i)
    i+=1    #i-=1 will print infinte loop

i=1 #print from 1 to 100
while i<=100:
    print(i)
    i+=1
   
i=100   
#reverse
while i>=1:
    print(i)
    i-=1
n=int(input("no"))
i=1
while i<=10:
    print(n*i)    #multiplication
    i+=1

n=2
while n<=5:
    print(n)
    n+=1

j=3
while j<=19:
    print(j)
    j+=2

k=0
while k<=5:

    if(k%2==0):
        k+=1            #using cotinue
        continue
    print(k)
    k+=1