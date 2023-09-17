#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)#

x = input("Check if palindrome: ")
x = x.replace(" ","").replace("'","").replace(".","").lower()
if x == x[::-1]:
    print("This is palindrome")
else:
    print("This is not palindrome")