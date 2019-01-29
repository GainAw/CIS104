print("What is you first name: ")
first_name = input()
print("What is you last name: ")
last_name = input()
print("What is you age name: ")
age = int(input())
dage = age*7
print("Hello {} {}, nice to meet you! You might be {} but in dog years you are {}.".format(first_name, last_name, age, dage))