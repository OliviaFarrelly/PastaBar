def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def print_menu(l):
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)

    return None


def print_with_indexes(l):
    for x in range(0, len(l)):
        output = "{:2}: {:10} ${:2f}".format(x, l[x][0].upper(), l[x][2])
        print(output)


def print_with_index(customer_o):
    for x in range(0, len(customer_o)):
        output = "{:2}: {:10} {:10}".format(x, customer_o[x][1], customer_o[x][0].upper())
        print(output)


def add_pasta(l, customer_o):
    print_with_indexes(l)
    message = "What pasta would you like to add to your order"
    option = get_integer(message)
    message = "How many {} would you like to add: ->".format(l[option][0])
    quantity = get_integer(message)
    temp = (l[option][0], quantity, l[option][2])
    customer_o.append(temp)
    output = "You have added {} {} to your order".format(quantity, l[option][0])
    print(output)


def review_order(customer_o):
    total = 0
    for x in customer_o:
        output = "{} {} @ ${} each : ${} ".format(x[1], x[0], x[2], x[1]*x[2])
        subtotal = x[1]*x[2]
        total += subtotal
        print(output)
    total_output = "Your order will cost ${}".format(total)
    print(total_output)


def main():
    pasta_lists = (["Fusilli Pesto", "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, "
                    "parmesan", 19],
                   ["Conchilglie alla Bolognese", "Small, shell pasta. Northern italian beef and pork sauce, "
                    "parmesan", 22],
                   ["Spaghetti Pomodoro", "Long, thin pasta. Classic tomato and basil sauce, parmesan", 16],
                   ["Pappardelle Ricci D'Angelo", "Short, frizzy pasta. Slow cooked lamb ragu, "
                    "rosemary, olives, sweet garlic, parmesan", 26],
                   ["Fettuccine Carbonara", "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan", 20],
                   ["Ravioli di Ricotta", "Spinach and ricotta (filled) pasta, brown butter sauce, sage, "
                    "hazelnuts, parmesan.", 20],
                   ["Rigatoni alla Caponata", "Short, tube pasta. Agrodolce tomato sauce, eggplant, "
                    "ricotta salata, pine nut", 21],
                   ["Linguine Gamberi", "Long flat pasta. Tomato, garlic and chilli sauce, prawns, anchovies, "
                    "capers, olives, parmesan", 23])
    customer_order = []
    run = True
    while run is True:
        menu = ["P: Print Menu", "A: Add Pasta To Order", "R: Review Order", "Q: Quit"]
        for x in menu:
            print(x)
        choice = input("What would you like to do?")
        if choice == "P":
            print_menu(pasta_lists)
        elif choice == "A":
            add_pasta(pasta_lists, customer_order)
        elif choice == "R":
            review_order(customer_order)
        elif choice == "Q":
            run = False
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()
