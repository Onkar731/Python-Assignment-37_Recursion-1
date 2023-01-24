"""
Write a recursive function to print MySirG N times on the screen
"""

# defining a function "print_mysirg()" which takes a number as an argument
# and print MySirG on the screen
def print_mysirg(num):
    if num != 0:
        print("MySirG")
        print_mysirg(num-1)
        

# taking input from the user
N = int(input("Enter a number : "))

# calling print_mysirg() to print it N times
print_mysirg(N)