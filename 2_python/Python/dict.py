info={
    "key":"value",
    "Skills":["Pyhton","Fitness ","Communication"],
    "name":"sravan",
    "age":21                       #We can add anything inside dictionaries
}
print(info)

print(info["key"])

sravan={
    "age":21,
    "gender":"male",
    "height":184,                                     #nested dictionaties
    "interest":{
        "Bussiness":"Money,respect",
        "job":"experience"
    }
}
print(sravan)

print(sravan.keys())      #keys which gives all keys
print(len(list(sravan.keys())))

print(list(sravan.values()))


chest={30,32.5,30}
print(chest)
sravan=set()
print(type(sravan))
chest.clear()
sravan.add(1)
sravan.add(2)
sravan.remove(2)
sravan.add(3)
print(sravan)

dicts={
    "cat":"an animal",
 "table" : ["a piece of furniture","lis t of numbers" ]
}
print(dicts)

name={
    "sravan":"Male",
    "age":21
}
print(name)


sravan2={
    "age":"low",
    "gender":"male",
    "sravan3":{
        "age1":"low1",
        "gender1":"male1"

    }
}
print(sravan2)

mom=set()
mom.add(2)
mom.add(3)
print(mom)    #elements can be added to a set if empty and it is immutale but 

mom1={"high","best"}
print(type(mom1))  #in this case we cannot perform opereations


srkr={}
x=int(input(" enter phy:"))
srkr.update({"phy":x})
x=int(input(" enter ds:"))   #adding elements in dict
srkr.update({"ds":x})

print(srkr)


values={9,"9.0"}   #two elements difference
print(values)




