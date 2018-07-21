import time

def insertsort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

def finder(list,input):
    for i in range(0,len(list)):
        if list[i] == float(input):
            return i
        else:
            continue
    if input not in list:
        print("Nope.")

def factorial(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    else:
        return number * factorial(number - 1)

def factorialloop(number):
    counter = 1
    total = 1
    for i in range(number):
        total = total * (counter + 1)
        counter +=1
        print(counter)
    return total

tick = time.time()
factorial(1000)
tock = time.time()
print(tick-tock)
