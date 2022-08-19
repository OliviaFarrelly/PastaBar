def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_menu(l):
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)
    return None


def print_details(customer_details):
    for x in customer_details:
        output = "{}: Name: {} Phone number: {} Address: {}".format(x[0], x[1], x[2], x[3])
        print(output)


def print_with_indexes(l):
    for x in range(0, len(l)):
        output = "{:2}: {:10} ${:2}".format(x, l[x][0].upper(), l[x][2])
        print(output)


def print_with_index(customer_o):
    for x in range(0, len(customer_o)):
        output = "{:2}:{:10} {:10} ${:10}".format(x, customer_o[x][1], customer_o[x][0], customer_o[x][2])
        print(output)


def add_pasta(l, customer_o):
    print_with_indexes(l)
    print("-" * 100)
    message = "What pasta would you like to add to your order: "
    option = get_integer(message)
    message = "How many {} would you like to add: ->".format(l[option][0])
    l[option][1] = get_integer(message)
    temp = (l[option][0], l[option][1], l[option][2])
    customer_o.append(temp)
    output = "You have added {} {} to your order: ".format(l[option][1], l[option][0])
    print(output)


def get_details(customer_details):
    message = "Would you like Pick up or delivery P/D: "
    option = get_string(message)
    print("-" * 100)
    if option == "P":
        message = "What is your name: "
        name = get_string(message)
        message = "What is your phone number: "
        phone_number = get_string(message)
        temp = ("Pick up", name, phone_number)
        customer_details.append(temp)
        return 0
    elif option == "D":
        message = "What is your name: "
        name = get_string(message)
        message = "What is your phone number: "
        phone_number = get_string(message)
        message = "Where would you like your order delivered to: "
        address = get_string(message)
        temp = ("Delivery", name, phone_number, address)
        # print confirmation message
        customer_details.append(temp)
        return 3


def review_order(customer_o, extras, customer_details):
    total = 0
    for x in customer_o:
        output = "{} {} @ ${} each : ${} ".format(x[1], x[0], x[2], x[1]*x[2])
        subtotal = x[1]*x[2]
        total += subtotal
        print(output)
    total_output = "Your order will cost ${}: ".format(total)
    print("-" * 100)
    print(total_output)
    print_details(customer_details)
    if extras != 0:
        total += extras
        output = "Due to a ${} extra charge your total will now be ${}: ".format(extras, total)
        print(output)


def remove_pasta(customer_o):
    print_with_index(customer_o)
    print("-" * 100)
    message = "What pasta would you like to remove from your order: "
    option = get_integer(message)
    customer_o.pop(option)


def update_pasta(customer_o):
    print_with_index(customer_o)
    print("-" * 100)
    message = "What pasta would you like to update? "
    option = get_integer(message)
    output = "You currently have {} {} ordered: ".format(customer_o[option][1], customer_o[option][0])
    print(output)
    message = "How many {} would you like now? ".format(customer_o[option][0])
    new_value = get_integer(message)
    customer_o[option][1] = new_value


def confirmation(customer_o, customer_details):
    if len(customer_o) > 0 and len(customer_details) > 0:
        message = "Would you like to place your order Y/N: "
        response = get_string(message)
        if response == "Y":
            customer_o.clear()
            customer_details.clear()
            print("-" * 100)
            message = "Would you like to place a new order Y/N: "
            option = get_string(message)
            if option == "Y":
                print(main)
            if option == "N":
                print("Thank you")
                exit()
            # figure out hwo to quit
        elif response == "N":
            return
    elif len(customer_o) <= 0 and len(customer_details) <= 0:
        print("You haven't placed your order or entered you details yet please do so: ")
        return


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
    customer_details = []
    extras = 0
    run = True
    while run is True:
        menu = ["P: Print Menu", "A: Add Pasta To Order", "RE: Remove Pasta From Order", "U: Update Order",
                "D: Get customer details", "R: Review Order", "C: Confirm order", "Q: Quit"]
        print("-" * 100)
        for x in menu:
            print(x)
        choice = input("What would you like to do? ")
        print("-" * 100)
        if choice == "P":
            print_menu(pasta_lists)
        elif choice == "A":
            add_pasta(pasta_lists, customer_order)
        elif choice == "RE":
            remove_pasta(customer_order)
        elif choice == "U":
            update_pasta(customer_order)
        elif choice == "D":
            extras = get_details(customer_details)
        elif choice == "R":
            review_order(customer_order, extras, customer_details)
        elif choice == "C":
            confirmation(customer_order, customer_details)
        elif choice == "Q":
            run = False
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    main()
