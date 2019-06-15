khana = ["roti","sabzi","chawal"]

for item in khana:
    if item == "roti":
        print(item)
        break
else: # it will execute when for loop goes properly. or their is no break in loop
    print("Your item is not found")