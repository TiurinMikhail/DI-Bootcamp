#Perfect Number
x = int(input('Enter the Number: '))
def perfect_number(x):
    list_divisors = []
    for i in range(1, x):
        if x % i == 0:
            list_divisors.append(i)
    if sum(list_divisors) == x:
        return True
    else:
        return False

for i in range(1,10000):
    if perfect_number(i):
        print(i)
