f = open("abaa.txt", "r")
# Reading from file
#print(f.read())
# Reading from first 5 letters
#print(f.read(5))
# Reading from first line
#print(f.readline())
# Reading from first two lines
#print(f.readline())
#print(f.readline())
for x in f:
    print(x)
# its good practice to close files always    
f.close()