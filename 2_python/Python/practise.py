light=input("light:")
if(light=="green"):
    print("GO")
elif(light=="Yellow"):
    print("WAIT")
else:
    print("StOP")

num=int(input("num:"))
if(num%7==0):
    print("yes")
else:
    print("no")
 
workout=input("Workout:")
if(workout=="chest"):
    print("MAchine Press")
elif(workout=="Back"):
    print("lat pull down")
else:
    print("legs")

pal=[1,2,1]
srav=pal.copy()
srav.reverse()

if(pal==srav):
    print("yes")
else:
    print("NO")


Gym={
    "workout":"Push",
    "variations":"6",
    "Muscle Group":["chest","shoulder","Triceps"]
    
}
print(Gym)

'10'+'20'