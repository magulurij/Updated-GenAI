heros=["a","b","c","d"]
def print_len(list):
    print(len(list))

print_len(heros)

def print_ele(list):
    for item in list:
        print(item,end="")
print_ele(heros)


dict={
    "sravan":"hero",
    "age":19,
    "tuple":(1,2,3,4,5),
    "dict2":{
        "age":[31,26]
    }

}
print(dict)


curry=input("curry:")
if (curry=="chicken"):
    print("eat")
else:
    print("skip")





