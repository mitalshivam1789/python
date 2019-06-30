import json
# loads and load functions

data = '{"var1":"harry","var2":56}'
print(data)
print(type(data))# here data is a string
parsed = json.loads(data)
print(parsed)
print(type(parsed))# here we can see that parsedd is a dictionary
print(parsed["var1"])
#parsed1 = json.load(data)
#print(parsed1)
#---------json.dumps
data2 = {
    "channel_name":"CodeWithme",
    "cars":["bmw","audi","ferrari"],
    "fridge":("roti","bread","milk")
}
jscomp = json.dumps(data2) # used to converet the data into json formate
print(jscomp)
# task 1 -- difference between json.load() and json.loads
# task 2 -- what is sort keys parameter in dumps
