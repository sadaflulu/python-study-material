#accessing item in a list
# fruits=["apple","banana","mango"]
# print(fruits[0])
#change items in a list
# fruits=["apple","banana","mango"]
# fruits[1]="mango"
# print(fruits)

#adding items to a list
#append
# fruits=["apple","banana","mango"]
# fruits.append("orange")
# print(fruits)
#insert
# fruits=["apple","banana","mango"]
# fruits.insert(1,"grape")
#pop() removes an item  using its index
#showed the removed item
# fruits=["apple","banana","mango"]
# x=fruits.pop(1)
# print(x)
#without index the last one element will delete-pop
# fruits=["apple","banana","mango"]
# x=fruits.pop()
# print(x)
#del--it remove an item using   its index
#it can also delete a range of items
#show after removed element
# x=fruits.pop(1)
# fruits=["apple","banana","mango"]
# del fruits[1]
# print(fruits)
# numbers=[10,20,30,40,50]
# del numbers[1:4]
# print(numbers)
#remove() removes an item an item by its value,not its index,
# fruits=["apple","banana","mango"]
# fruits.remove("banana")
# print(fruits)
#create a lisit of five student names and use pop() to remove the last student . print tthe removed name and the updates list 
# students=["sadaf","hiba","hamdan","liba","kafi"]
# x=students.pop()
# print(x)
#create a list[10,20,30,40,50].remove the first occurence od 20, then usr pop() to remove last digit,
numbers=[10,20,30,40,50]
del numbers[1]
numbers.pop()
print(numbers)
#create a list[10,20,30,40,50].show the remove the first occurence od 20 ,and show remaining elements
# numbers=[10,20,30,40,50]
# x=numbers.pop(1)
# print("dlted item:-",x)
# print("remaning item:- ",numbers)


