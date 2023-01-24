"""
Write a recursive function to print first N odd natural numbers in reverse order
"""

# defining a function "print_odd_naturals_rev()" to print first N odd natural 
# numbers which takes a number as an argument and print odd natural numbers
def print_odd_naturals_rev(num):
    if num == 1:
        print(num, end=' ')
    else:
        print(num*2-1, end=' ')
        print_odd_naturals_rev(num-1)
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_odd_naturals_rev() to print odd natural numbers
print_odd_naturals_rev(N)