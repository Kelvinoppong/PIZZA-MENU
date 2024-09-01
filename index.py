def Mypizza_menu():
    print("Welcome To Pizzaman and Chickenman")
    name = input("Please Enter Your name: ")
    print(f"{name}, you are welcome")
    print('Here are the list of Pizza that we have')
    menu = ['Neapolitan Pizza',
            'Chicago-Style Pizza', 'New York-Style Pizza', 'Sicilian Pizza',
            'Greek Pizza', 'California Pizza', 'St. Louis Pizza',
            'Detroit-Style Pizza']

    for i, element in enumerate(menu, start=1):
        print(f"{i}.", element)

    choice = int(input('Please Select your Choice from 1-8: '))

    if 1 <= choice <= len(menu):
        selected_pizza = menu[choice-1]
        print(f'{name}, you have selected {selected_pizza}')

        extra_order = input('Would you like to place an additional order for drinks and wings? Yes or No: ')

        if extra_order.lower() == 'yes':
            print('Here are additional items you can place an order for')
            menu2 = ['Water', 'Coke', 'Strawberry', 'Wings', 'Sprite', 'Alvaro', 'Hennessy']
            for x, element in enumerate(menu2, start=1):
                print(f'{x}.', element)
            choice2 = int(input("Please Select your choice from 1-7: "))
            if 1 <= choice2 <= len(menu2):
                selected_order = menu2[choice2-1]
                print(f'{name}, you have selected {selected_order}')
                print('Your waiting time will be 7min')
        else:
            print('Your waiting time will be 10 mins')

Mypizza_menu()
