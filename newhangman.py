import random

def hangman():
    empty = """       _____
      |    \|
            |
            |
            |
    ________|___"""
    print("Welcome to Hangman!")
    level = input("Please choose beginner, intermediate, or advanced. ")
    if level == "beginner":
        print("The category for the beginner level is colors.")
        print(empty)
        words = ['violet',"pink","silver","navy","gray","maroon","brown","orange","pink","magenta","turquoise","ruby","yellow",'lavender','olive']
        game(words)
    elif level == "intermediate":
        print("The category for the intermediate level is tools.")
        print(empty)
        words = ["wrench","screwdriver","hammer","clamp","machete","drill","saw","scissors","knife","nail","pliers",'washer','bolt','chisel','vise']
        game(words)
    elif level == "advanced":
        print("The category for the advanced level is animals.")
        print(empty)
        words = ["antelope",'badger',"buffalo",'caterpillar','firefly','gecko','hedgehog','oyster','reindeer','wombat','crocodile','jellyfish']
        game(words)
    else:
        print("Error 404. Level not found.")

def game(words):
    number = random.randint(0,len(words) - 1)
    choice = words[number]
    lettercheck = [] #check if used before
    count = 0
    win = 0
    life = 6
    answer = "_ " * len(choice) + """
    """
    print("""
    """ + answer)
    while life > 0:
        letter = input("Choose a letter. ")
        if letter in lettercheck:
            print("You have already used this letter. Please choose another.")
        else:
            if letter in choice:
                lettercheck.append(letter)
                count = 0
                while count < len(choice):
                    if letter == choice[count]:
                        answer = list(answer)
                        answer[count*2] = letter
                        answer = ''.join(answer)
                        count +=1
                        win +=1
                    else:
                        count +=1
                print("""
    """ + answer)
                if win == len(choice):
                    print("Good job, you won! Your word was %s." % choice)
                    break
            else:
                life = life - 1
                letterchecker(letter,lettercheck,life,choice)
                if life <= 0:
                    break

def letterchecker(letter,lettercheck,life,choice):
    one = """       _____
      |    \|
      O     |
            |
            |
    ________|___
             """
    two = """       _____
      |    \|
      O     |
      |     |
            |
    ________|___
             """
    three = """       _____
      |    \|
      O     |
      |-    |
            |
    ________|___
             """
    four = """       _____
      |    \|
      O     |
     -|-    |
            |
    ________|___
             """
    five = """       _____
      |    \|
      O     |
     -|-    |
     /      |
    ________|___
             """
    six = """       _____
      |    \|
      O     |
     -|-    |
     / \    |
    ________|___
             """
    lettercheck.append(letter)
    if life == 0:
        print(six)
        print("GAME OVER. Your word was %s." % choice)
    elif life == 1:
        print(five)
        print("Your letter is not in the word.")
    elif life == 2:
        print(four)
        print("Your letter is not in the word.")
    elif life == 3:
        print(three)
        print("Your letter is not in the word.")
    elif life == 4:
        print(two)
        print("Your letter is not in the word.")
    elif life == 5:
        print(one)
        print("Your letter is not in the word.")
    elif life == 6:
        print("six lives")
    else:
        ("You broke the game.")

def main():
    againe = "yes"
    while againe == "yes":
        hangman()
        againe = input("Play again? ")

if __name__ == '__main__':
    print
    main()
