def print_menu(l):
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)

    return None


def main():
    pasta_lists = (["Fusilli Pesto", "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, "
                    "parmesan", 19],
                   ["Conchilglie alla Bolognese", "Small, shell pasta. Northern italian beef and pork sauce, "
                    "parmesan", 22],
                   ["Spaghetti Pomodoro", "Long, thin pasta. Classic tomato and basil sauce, parmesan", 16],
                   ["Pappardelle Ricci D'Angelo", "Short, frizzy pasta. Slow cooked lamb ragu, "
                    "rosemary, olives, sweet garlic, parmesan", 26],
                   ["Fettuccine Carbonara", "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan", 20])
    run = True
    while run is True:
        menu = ["P: Print Menu", "Q: Quit"]
        for x in menu:
            print(x)
        choice = input("What would you like to do?")
        if choice == "P":
            print_menu(pasta_lists)
        elif choice == "Q":
            run = False
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()
