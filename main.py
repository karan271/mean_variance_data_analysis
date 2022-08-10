temp1 = 0
temp2 = 1
for i in range(0, 11):
    current = temp1 + temp2
    print(current, end=" ")
    temp1 = temp2
    temp2 = current

print()
def create_palindrome(length):
    for j in range(1, length+1):
        if (j<=length/2):
            print(j, end="")
        else:
            print(length+1-j, end="")
    return

length = int(input('Please enter a number:'))
create_palindrome((length*2)-1)

