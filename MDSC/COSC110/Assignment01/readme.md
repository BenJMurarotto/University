### Running burger.py
Burger.py is a Python script which acts to ask the customer questions regarding their order, storing their inputs and calculating the price of their order. To run the script you will need an environment which runs Python 3.
Simply input the following to execute the program:
'python3 burger.py'

How burger.py works:

1. Welcome Message: The script starts by welcoming the customer to Codetown Burger Co. and asks for the number of burgers they would like to order (between 1 and 10).

2. Requesting Order Inputs: The first segment of the code contains all of the possible valid inputs that a customer can respond with. If you wanted to alter the options in the lists. For example if you wanted to add mayonnaise to the list sauce_options this is how it would look:
    sauce_options = ['tomato', 'barbeque', 'none'] => sauce_options = ['tomato', 'barbeque', 'mayonnaise', 'none']

The second segment will loop through and ask the customer what options they would like on their burger for n times where n is the number of burgers ordered. The code contains error handling so that if the customer inputs something not in the valid options lists above, they will be repromted to answer again.
It is possible to add extra options by simply copying a block of code and creating a valid option list in the initial segment as discussed above.
A segment for adding bacon to the option list would look like so:

    valid_bacon_option = False
    while not valid_bacon_option:
        bacon_option = input(f'Should Burger {order_number} have bacon [yes, no]? ')
        if bacon_option.lower() in other_options:
            valid_bacon_option = True
        else:
            print('Invalid entry, please choose again!')

You would also require bacon_options in the lists section of the code.

    bacon_options = ['yes', 'no', 'y', 'n']

It is important to state the to customer in the input section which choices are valid to avoid confusion.

3. Storing Order Inputs: The third section of code is a dictionary which stores the burger orders. This is important for relaying back to kitchen staff to prepare the burgers. It acts as the script for the program uses to read the order and calculate price. Above amendments will also need to be applied to the dictionary like so:

    order[order_number] = {'Bun' : bun_type, 'Sauce' : sauce_type, 'Number of patties' : 
                           patty_option, 'Number of cheese slices' : cheese_option, 'Tomato' : tomato_option, 'Lettuce' : lettuce_option, 'Onion' : onion_option, 'Bacon' : bacon_option } 

The order will be return to Codetown in the same format as the dictionary so if the 2nd burger in an order contains bacon, it will appear as:  
    order 2 = {'Bun' : 'milk', ..., 'Bacon' : 'yes'}

4. Calculating Total Price: Finally, the last important segment of code contains the algorithm which calculates price. Simply add a separate 'if' line and designate the price of that item. Following the bacon example:

     if bacon_option == 'y' or 'yes':
        total_price + 3

