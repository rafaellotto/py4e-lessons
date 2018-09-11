largest = None
smallest = None
numbers = []

while True:
    num = input("Enter a number: ")

    if num == "done" :
        for item in numbers:
            if largest is None or item > largest:
                largest = item
        for item in numbers:
            if smallest is None or item < smallest:
                smallest = item
        break

    try :
        num = int(num)
        numbers.append(num)
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
