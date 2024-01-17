#Create a program that swaps the values of two variables.
x = 15
y = 30

print("the values of x and y are {},{} before swapping".format(x,y))

x, y = y, x
print("the values of x and y are {},{} after swapping".format(x,y))