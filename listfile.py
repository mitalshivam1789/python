grocery = ["harpic","vim bar","deodrant","bhindi","lollypop", 56]
print(grocery)
print(grocery[3])
print(grocery[1:5])
numbers=[2,4,6,2,6,5,8,7]
print(numbers)
print(numbers[1:6])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(3)
print(numbers)
print(len(numbers))
print(max(numbers))
numbers.insert(2,73)
print(numbers)
numbers.remove(2)
print(numbers)
print(numbers.pop())
# we cann't change the values of a tuple but we can chage the values of a list
numbers[3]="shivam"
print(numbers)
# tuples are immutable
tp = (1,2,3,5,2,5,32,21)
print(tp)
tp1 = (1,)
print(tp1)