# MEE 12/02/21

def sum_to(value):
    total = 0
    x = 0
    while x <= int(value):
        total += x
        x += 1
    return total

value = input("Enter an integer: ")
print(sum_to(value))

