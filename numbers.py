def decorate_ticket(function):

    def ticket(number):
        print("Your number is")
        function(number)
        print("Wait and someone will be shortly")
    return ticket


def perfume():
    n = 0
    while True:
        n += 1
        yield n


def print_number(chosen_part):
    if chosen_part == 1:
        num = next(perfumes_generator)
        print(f"P-{num}")
    elif chosen_part == 2:
        num = next(meds_generator)
        print(f"M-{num}")
    else:
        num = next(cosmetics_generator)
        print(f"C-{num}")


def medicines():
    n = 0
    while True:
        n += 1
        yield n


def cosmetics():
    n = 0
    while True:
        n += 1
        yield n


decorated_function = decorate_ticket(print_number)
perfumes_generator = perfume()
meds_generator = medicines()
cosmetics_generator = cosmetics()
