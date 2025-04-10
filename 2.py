def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
print('please enter a number')
x = int(input())
print(fact(x))