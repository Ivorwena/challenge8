import numbers
import os


def choose():
    my_choice = "p"
    while my_choice not in [1, 2, 3, 4]:
        try:
            my_choice = int(input("Hello! Choose which area interests you:\n1 - perfumes\n2 - medicine\n3 - cosmetics\n"
                                  "4 - exit\n"))
        except ValueError:
            print("That is not one of the possible choices")
            continue
        if my_choice not in [1, 2, 3, 4]:
            print("That is not one of the possible choices")
    return my_choice


while True:
    choice = choose()
    if choice == 4:
        break
    numbers.decorated_function(choice)
    input("Press <ENTER> to continue...")
    os.system('clear')
