def multiply(numbers):
    total= numbers[0]
    for x in numbers:
       total=total*x
    return total
print(multiply([1,2,3]))