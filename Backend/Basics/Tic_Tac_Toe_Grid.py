n = int(input("Enter the grid size: "))

# Function to convert a half-width char into a full-width char
def full(s):
    return chr(ord(s) + 65248)

for i in range(2*n-1):
    if (i % 2 == 0):
        for j in range(n-1):
            print(' ', full('|'), end = "")
    else:
        for k in range(n):
            
            # Printing the unicode character for horizontal line char
            print('\U0000FF0D', ' ', end="")
    print()
