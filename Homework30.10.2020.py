# Exercise 1
num = int('2000')

while num < 5001:
    check = [int(i) for i in str(num)]
    if (check[0]%2 == 0 and check[1]%2 == 0 and check[2]%2 == 0 and check[3]%2 == 0):
        print(num, end=", ")
    num += 1
print( )
print( )
 
# Exercise 2
numbers = [20, 40, 60, 80, 100, 5]
i = len(numbers)
smallest = numbers[0]
biggest = numbers[0]

while i > 0:
    if(numbers[i - 1] > biggest):
        biggest = numbers[i - 1]
    elif(numbers[i - 1] < smallest):
        smallest = numbers[i - 1]
    i -= 1
print(biggest - smallest)
print( )

# Exercise 3
string = input("Enter a string with numbers: ")
i = len(string)
num_amount = 0
letter_amount = 0
space_amount = 0

while i > 0:
    if(string[i - 1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
        num_amount += 1
    elif(string[i - 1] in (" ", ",", ".", "/", "?", "!", ":", "'", )):
        space_amount += 1
    else:
        letter_amount += 1
    i -= 1
print("Letters: ", letter_amount)
print("Numbers: ", num_amount)