#Creating a list
numbers = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Grapes", "Mangoes"]
#print(fruits)
#print(fruits[0], fruits[1], fruits[2], fruits[3])
#print(len(fruits))
fruits.append("Peers")
fruits.remove("Oranges")
fruits.insert(2, "Strawbery")
fruits.pop(2)
fruits.reverse()
fruits.sort()
fruits.sort(reverse=True)
fruits[0] = "Banana"
print(fruits)
print(type(fruits))