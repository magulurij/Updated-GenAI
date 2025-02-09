marks=[12,13,15,161]
print(marks)         ##list

print(marks[1])
student=["sravan",19,"kumar"]  #lists are mutable
student[0]="kumar"
print(student)

print(marks[1:2])      #slicing

sravan=[1,2,2,3,4]
sravan.append(6)      #adding element at last is append
sravan.reverse()      ##reverse of elements
sravan.sort()      #arriging ascendind oder
sravan.insert(1,5)
sravan.sort(reverse=True)
sravan.remove(2)
sravan.pop(1)
print(sravan)


movies=[]
mov1=input("movie name:")
mov2=input("movie name:")
mov3=input("movie name:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

pal=[1,2,1]
rev=pal.copy()      #palindorme
rev.reverse()
if(rev==pal):
    print("yes")
else:
    print("no")


tuple=("A","B","C","A")
print(tuple.count("B"))
