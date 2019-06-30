list_value=input("enter a list with spaces between numbers.")
list_value=list_value.split(" ")
for i in range(len(list_value)):
    list_value[i] = int(list_value[i])
print(list_value)
print(type(list_value[1]))
list_value.reverse()
print(list_value)
list_value.reverse()
print(list_value[::-1])
len=len(list_value)
if len%2 == 0:
    for i in range(int(len/2)):
        temp = list_value[i]
        list_value[i]=list_value[len-1-i]
        list_value[len-1-i] = temp
elif len%2!=0:
    for i in range(int((len-1)/2)):
        temp = list_value[i]
        list_value[i]=list_value[len-1-i]
        list_value[len-1-i] = temp

print(list_value)

#print("By method 1 - ",reverse_list1)