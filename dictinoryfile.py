dictionary={"name":"shivam","branch": "ece","roLlno":"ue175106","marks":6.4,"students":{"name":["ravi","shayam","rajan","rajnish"],"marks":[76.66,87,78]}}
print(dictionary)
print(dictionary["name"])
print(dictionary["students"]["name"][2])
dictionary["ankit"]="food"
print(dictionary)
dictionary["students"]["ram"]="love"
print((dictionary))
dictionary["students"]["name"].append("ghanshayam")
print(dictionary)
del dictionary["ankit"]
print(dictionary)
d2=dictionary.copy()
print(d2)
print(d2.keys())
print(d2.values())
d2.update({"shivam":"good"})
print(d2)
print(d2.items())
print(d2.get("students"))
for x in d2:
    print(x)
    print(d2[x])
if "name" in d2:
    print("no problem")
print(len(d2["students"]))
d2.pop("name")
