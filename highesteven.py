

# To find Highest Even
def highest_Even(numList):
    highest_number = 0
    for item in numList:
        if(item % 2 == 0 and item > highest_number):
            highest_number = item
    return highest_number


print(highest_Even([10, 25, 35, 40, 67]))
