animals = ["Lion", "Elephant", "Rabbit", "Leopard"]
x = len(animals)
animals.pop(1)  #Removes the element at the specified position
animals.remove("Rabbit") #Removes the first item with the specified value
animals.sort() #Sorts the list
animals.reverse() #Reverses the order of the list
animals.append() #Adds an element at the end of the list
animals.insert() #Adds an element at the specified position
animals.index()  #Returns the index of the first element with the specified value
animals.extend() #Add the elements of a list (or any iterable), to the end of the current list
animals.count()  #Returns the number of elements with the specified value
animals.copy()  #Returns a copy of the list
animals.clear() #Removes all the elements from the list
print(animals)
print(x)
print(type(animals))