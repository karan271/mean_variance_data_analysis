a = int(input())
b = int(input())

c = abs(a * b)
if a > b:
    d = a % b
else:
    d = b % a

e = c // d
print(f'HCF: {d}')
print(f'LCM: {e}')
