# myList = [ele*2 for ele in range(10)]

myList = [int(ele) for ele in input("Enter numbers separated by space: ").split() if int(ele) % 2 == 0]
# This code takes input from the user, splits it by spaces, converts each element to an integer, and filters out even numbers.

print(myList)