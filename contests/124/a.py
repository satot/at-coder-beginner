# input a, b: num
# output: num

def max_coins(a, b):
    if a > b:
        return a + (a-1)
    elif a == b:
        return a + b
    else:
        return b + (b-1)

print(max_coins(5,3))
print(max_coins(3,4))
print(max_coins(6,6))
