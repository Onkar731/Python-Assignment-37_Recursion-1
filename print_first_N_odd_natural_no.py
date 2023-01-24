"""
Write a recursive function to print first N odd natural numbers
"""

# defining a function "print_odd_naturals()" to print first N odd natural numbers
# which takes a number as an argument and print odd natural numbers
def print_odd_naturals(num):
    if num == 1:
        print(num, end=' ')
    else:
        print_odd_naturals(num-1)
        print(num*2-1, end=' ')
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_odd_naturals() to print odd natural numbers
print_odd_naturals(N)