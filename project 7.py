no_of_items = input("no of items you what type of items they are")
list1=[]
for i in range(no_of_items):

    type_of_item = input(f"enter type of {i} item is :")
    list1.append(type_of_item)

for i in list1:
    if i == "list":
        list2 = []

        data1 =input("enter the item to save")
        list1.append(data1)
        print()
