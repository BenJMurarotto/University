#Defining valid responses for burger order
order = {} #Dictonary to store order inputs and read them later to calc price
order_number = 1
bun_options = ['milk', 'gluten free']
sauce_options = ['tomato', 'barbeque', 'none']
patty_options = range(4)
cheese_options = range(4)
other_options = ['yes', 'no', 'y', 'n']

#Starting customer interaction
print('Welcome to Codetown Burger Co!')
num_burgers = int(input('How many burgers would you like to order [1-10]?: '))

#This loop prompts inputs for each order specified in num_burgers
while num_burgers > 0:
    valid_bun_type = False
    while not valid_bun_type:
        bun_type = input(f'What bun type should be included for Burger {order_number}, [milk or gluten free]? ')
        if bun_type.lower() in bun_options:
            valid_bun_type = True
        else:
            print('Invalid entry, please choose again!')

    valid_sauce_type = False
    while not valid_sauce_type:
        sauce_type = input(f'What sauce should be included on Burger {order_number}, [tomato, barbeque or none]? ')
        if sauce_type.lower() in sauce_options:
            valid_sauce_type = True
        else:
            print('Invalid entry, please choose again!')
            

    valid_patty_option = False
    while not valid_patty_option:
        patty_option = int(input(f'How many patties would you like on Burger {order_number}, [0-3]]? '))
        if patty_option in patty_options:
            valid_patty_option = True
        else:
            print('Invalid entry, please choose again!')

    valid_cheese_option = False
    while not valid_cheese_option:
        cheese_option = int(input(f'How many cheese slices would you like on Burger {order_number}, [0-3]]? '))
        if cheese_option in cheese_options:
            valid_cheese_option = True
        else:
            print('Invalid entry, please choose again!')

    valid_tomato_option = False
    while not valid_tomato_option:
        tomato_option = input(f'Should Burger {order_number} have tomato [yes, no]? ')
        if tomato_option.lower() in other_options:
            valid_tomato_option = True
        else:
            print('Invalid entry, please choose again!')

    valid_lettuce_option = False
    while not valid_lettuce_option:
        lettuce_option = input(f'Should Burger {order_number} have lettuce [yes, no]? ')
        if lettuce_option.lower() in other_options:
            valid_lettuce_option = True
        else:
            print('Invalid entry, please choose again!')

    valid_onion_option = False
    while not valid_onion_option:
        onion_option = input(f'Should Burger {order_number} have onion [yes, no]? ')
        if onion_option.lower() in other_options:
            valid_onion_option = True
        else:
            print('Invalid entry, please choose again!')

            
# We store each response as a separate order in the dictionary 'order{}'
    order[order_number] = {'Bun' : bun_type, 'Sauce' : sauce_type, 'Number of patties' : 
                           patty_option, 'Number of cheese slices' : cheese_option, 'Tomato' : tomato_option, 'Lettuce' : lettuce_option, 'Onion' : onion_option }
    num_burgers -= 1
    order_number += 1

# I used if statements to read each iteration of the dictionary to search for options that would alter the price e.g ordering a gluten free bun
total_price = (order_number - 1) * 5  # Base price for each burger

# Loop through each order to calculate the total price
for i in range(1, order_number):
    # Retrieve order details for the current burger
    current_order = order[i]

    # Add additional costs based on options
    if current_order['Bun'] == 'gluten free':
        total_price += 1
    if current_order['Number of patties'] > 1:
        total_price += (current_order['Number of patties'] - 1) * 3
    if current_order['Number of cheese slices'] > 1:
        total_price += (current_order['Number of cheese slices'] - 1)
    if current_order['Tomato'].lower() == 'y' or current_order['Tomato'].lower() == 'yes':
        total_price += 1
    if current_order['Lettuce'].lower() == 'y' or current_order['Lettuce'].lower() == 'yes':
        total_price += 1
    if current_order['Onion'].lower() == 'y' or current_order['Onion'].lower() == 'yes':
        total_price += 1

# Relaying the cost of the order and ending the transaction with the customer
print(f'The total cost for {order_number - 1} burger(s): ${total_price}')
print('Thank you for ordering at Codetown Burgers Co., we hope to see you again!')

    