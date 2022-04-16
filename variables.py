a = 10
b = 20
c = a + b
print(c)

floor = int(input("Floor: "))

 # Adjust floor if necessary.
if floor > 13 :
 actualFloor = floor - 1
else :
  actualFloor = floor

 # Print the result.
print("The elevator will travel to the actual floor", actualFloor)