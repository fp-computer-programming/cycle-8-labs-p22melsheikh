# MEE 12/1/21

def sum_to(num):
    total = 0
    for value in range(int(num) + 1):
        total += value
    return total    
        


number = input("Give me a number: ")
sum_to(number)
print(sum_to(number))