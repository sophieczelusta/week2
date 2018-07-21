def dollarpyr():
    size = int(input("How many lines of pattern?"))
    count = 0
    width = (2 * size) + 1
    constant = size
    for number in range(size):
        count += 1
        print((constant * " ") + (count * "$ ") + (constant * " "))
        constant -= 1
dollarpyr()
