def get_string(m, _min=1, _max=20):
    """
     validation for string inputs

    :param m: string
    :param _min: shortest string possible
    :param _max: longest string possible
    :return: string
    """
    getting = True
    while getting is True:
        my_string = input(m)
        if len(my_string) < _min:
            print("Your entry is too short, please try again: ")
        elif len(my_string) >= _max:
            print("Your entry is too long, please try again: ")
        else:
            return my_string


def get_integer(m, _min=0, _max=10):
    """
    Validation for integer inputs

    :param m: integer
    :param _min: lowest integer possible
    :param _max: highest integer possible
    :return: integer
    """
    getting = True
    while getting is True:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("You have not entered a valid integer. Please try again: ")
            continue
        if my_integer < _min:
            print("Your input is too small, please try again. ")
        elif my_integer >= _max:
            print("Your input is too large, please try again.")
        else:
            return my_integer


def print_menu(l):
    """
    printing out the pasta menu with price, description and name of the dish

    :param l: list
    :return: none
    """
    for x in l:
        print(x[0].upper())
        output = "{} ${}".format(x[1], x[2])
        print(output)
    return None


def print_details(customer_details):
    """
    function to print out customer details when they have entered their details

    :param customer_details: list
    :return: none
    """
    for x in customer_details:
        output = "{}: Name: {} Phone number: {} Address: {}".format(x[0], x[1], x[2], x[3])
        print(output)


def print_with_indexes(l):
    """
     function to print out the pasta menu with indexes so user can choose what they want to add to their order

    :param l: list
    :return: none
    """
    for x in range(0, len(l)):
        output = "{:2}: {:10} ${:2}".format(x, l[x][0].upper(), l[x][2])
        print(output)


def print_with_index(customer_o):
    """
    function to print the customer order out in a nice easy way for teh user to see and update if they need

    :param customer_o:
    :return: none
    """
    for x in range(0, len(customer_o)):
        output = "{:2}:{:10} {:10} ${:10}".format(x, customer_o[x][1], customer_o[x][0], customer_o[x][2])
        print(output)


def add_pasta(l, customer_o):
    """
    adding pasta to the customer order

    :param l: list
    :param customer_o: list
    :return: none
    """
    # printing out the pasta list
    print_with_indexes(l)
    print("-" * 100)
    # asking what pasta they would like to add to their order
    message = "What pasta would you like to add to your order: "
    option = get_integer(message)
    # asking hwo many they would like to add to their order
    message = "How many {} would you like to add: ->".format(l[option][0])
    quantity = get_integer(message)
    # creating a temporary list
    temp = [l[option][0], quantity, l[option][2]]
    # putting the information into the customers order
    customer_o.append(temp)
    # explaining what food they just added to their order
    output = "You have added {} {} to your order: ".format(temp[1], temp[0])
    print(output)


def get_details(customer_details):
    """
    getting the customers details

    :param customer_details: list
    :return: 0 or 3
    """
    # asking user whether their order will be picked up or delivered
    message = "Would you like Pick up or delivery P/D:"
    option = get_string(message)
    # making it case-insensitive
    option = option.upper()
    print("-" * 100)
    # loop
    # if they choose Pick up ask for name and phone number if delivery also ask for address
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
        # temporary list
        temp = ("Delivery", name, phone_number, address)
        # printing out their details
        # asking if they are correct
        # making it case-insensitive
        output = "{}: Name: {} Phone number: {} Address: {}".format("Delivery", name, phone_number, address)
        print(output)
        message = "Are your details correct Y/N:"
        response = get_string(message)
        response = response.upper()
        # loop
        # If they say yes details get put into the list
        # If they say no they can re-input there details
        if response == "Y":
            customer_details.append(temp)
        elif response == "N":
            print("You entered your details wrong try again")
            return get_details(customer_details)
        # adding 3 dollars to total price if the user chooses delivery
        return 3


def review_order(customer_o, extras, customer_details):
    """
    Reviewing teh customers order, there details, and giving them there total price

    :param customer_o: list
    :param extras: value
    :param customer_details: list
    :return: none
    """
    # making total price 0 to start with
    total = 0
    # making an output so user can see what each pasta costs individually and the cost for how many they got
    for x in customer_o:
        output = "{} {} @ ${} each : ${} ".format(x[1], x[0], x[2], x[1]*x[2])
        # quantity times the price of teh pastas
        subtotal = x[1]*x[2]
        # adding all the subtotals together
        total += subtotal
        print(output)
    # price of customers order
    total_output = "Your order will cost ${}: ".format(total)
    print("-" * 100)
    print(total_output)
    # printing out the customers details
    print_details(customer_details)
    # adding extras to price if user chose delivery
    # telling them that it cost three dollars extra
    if extras != 0:
        total += extras
        output = "Due to a ${} extra charge your total will now be ${}: ".format(extras, total)
        print(output)


def remove_pasta(customer_o):
    """
    Removing all the one kind of pasta from the order

    :param customer_o: list
    :return: none
    """
    # printing teh customers order out with indexes
    print_with_index(customer_o)
    print("-" * 100)
    # asking what pasta they would like to remove from there order using the index numbers
    message = "What pasta would you like to remove from your order: "
    option = get_integer(message)
    # removing the pasta from teh order
    customer_o.pop(option)


def update_pasta(customer_o):
    """
    updating the amount of one kind of pasta they have in their order

    :param customer_o: list
    :return: none
    """
    # printing teh customers order out with indexes
    print_with_index(customer_o)
    print("-" * 100)
    # asking what pasta customer would like to update
    message = "What pasta would you like to update? "
    option = get_integer(message)
    # letting them know how many they already have in their order
    output = "You currently have {} {} ordered: ".format(customer_o[option][1], customer_o[option][0])
    print(output)
    # asking how many they would like now
    message = "How many {} would you like now? ".format(customer_o[option][0])
    new_value = get_integer(message)
    # updating the order with teh new value
    customer_o[option][1] = new_value


def confirmation(customer_o, customer_details):
    """
    Confirming customers order and seeing if they want to place another order

    :param customer_o: list
    :param customer_details: list
    :return: none
    """
    # making sure there is information in both the lists
    if len(customer_o) > 0 and len(customer_details) > 0:
        # if there is information in both lists, asking teh user if they want to place their order
        message = "Would you like to place your order Y/N: "
        response = get_string(message)
        # making case-insensitive
        response = response.upper()
        if response == "Y":
            # clearing both lists
            customer_o.clear()
            customer_details.clear()
            print("-" * 100)
            # asking if they would like to place a new order
            message = "Would you like to place a new order Y/N: "
            option = get_string(message)
            # making case-insensitive
            option = option.upper()
            if option == "Y":
                # printing out the main again so customer can make a new order
                print(main())
            if option == "N":
                # quitting program if customer is finished placing orders
                print("Thank you")
                exit()
        # if user inst ready to place order taking them back to the main page to keep working on their order
        elif response == "N":
            return
    # if there is no information in teh lists letting user know they haven't entered details yet
    # taking the user back to the home page so they cna work on their order
    elif len(customer_o) <= 0 and len(customer_details) <= 0:
        print("You haven't placed your order or entered you details yet please do so: ")
        return


def main():
    """
    main menu of the ordering system
    where all the lists are kept

    :return: true or false
    """
    # Pasta lists with name, price and description
    pasta_lists = (("Fusilli Pesto", "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, "
                    "parmesan", 19),
                   ("Conchilglie alla Bolognese", "Small, shell pasta. Northern italian beef and pork sauce, "
                    "parmesan", 22),
                   ("Spaghetti Pomodoro", "Long, thin pasta. Classic tomato and basil sauce, parmesan", 16),
                   ("Pappardelle Ricci D'Angelo", "Short, frizzy pasta. Slow cooked lamb ragu, "
                    "rosemary, olives, sweet garlic, parmesan", 26),
                   ("Fettuccine Carbonara", "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan", 20),
                   ("Ravioli di Ricotta", "Spinach and ricotta (filled) pasta, brown butter sauce, sage, "
                    "hazelnuts, parmesan.", 20),
                   ("Rigatoni alla Caponata", "Short, tube pasta. Agrodolce tomato sauce, eggplant, "
                    "ricotta salata, pine nut", 21),
                   ("Linguine Gamberi", "Long flat pasta. Tomato, garlic and chilli sauce, prawns, anchovies, "
                    "capers, olives, parmesan", 23))
    # empty lists for customers details and their order and for teh extras if needed
    customer_order = []
    customer_details = []
    extras = 0
    # loop
    run = True
    while run is True:
        menu = ["P: Print Menu", "A: Add Pasta To Order", "RE: Remove Pasta From Order", "U: Update Order",
                "D: Get customer details", "R: Review Order", "C: Confirm order", "Q: Quit"]
        print("-" * 100)
        for x in menu:
            print(x)
        # asking what option the user would like to do first
        choice = input("What would you like to do? ")
        choice = choice.upper()
        print("-" * 100)
        # telling teh program what happens when teh user chooses each letter/each option
        # what function will run
        # what lists need to be used
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
        # quitting program when they are ready
        elif choice == "Q":
            run = False
        # what happens when an incorrect entry is entered
        else:
            print("Unrecognised entry")


if __name__ == '__main__':
    # running the mian program
    main()
    