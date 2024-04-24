# Here are a few constant variables - I re-used the same options as burger.py
bun_options = ['milk', 'gluten free']
sauce_options = ['tomato', 'barbecue', 'none']
patty_options = range(4)
cheese_options = range(4)
other_options = ['yes', 'no', 'y', 'n'] 
# These are all for error handling to make sure order.txt contains values accessible by the program

stored = {}
base_price = 5

# convert_to_tuple attempts to look for a readable file - later on we call the function and specify order.txt
def convert_to_tuple(order_path):
    try:
        with open(order_path, 'r') as file:
            for line in file: #For loop which iterates through each line of the text file
                tuple_items = [] #List to store data before we convert them to tuples
                ordered_line = line.strip().split(',') #Separates the line by the comma and stores them in a lists
                if (ordered_line[0] in bun_options and
                    ordered_line[1] in sauce_options and
                    int(ordered_line[2]) in patty_options and
                    int(ordered_line[3]) in cheese_options and
                    ordered_line[4] in other_options and
                    ordered_line[5] in other_options and
                    ordered_line[6] in other_options): #This if statement checks that the order.txt file has the correct items in orientation
                        for item in ordered_line: #As the text file was originally string format, this for loop changes the numbers to int and the yes/no to boolean types
                            if item.strip() in ['0', '1', '2', '3']:
                               tuple_items.append(int(item.strip()))
                            elif item.strip() == 'yes':
                                tuple_items.append(True)
                            elif item.strip() == 'no':
                                tuple_items.append(False)
                            else:
                                tuple_items.append(item.strip())
 
                        final_tuple = tuple(tuple_items) #We turn the list into a tuple and then store that tuple in the stored dictionary
                        if final_tuple in stored: #This if statement is used to count repeats of orders
                            stored[final_tuple] += 1
                        else:
                            stored[final_tuple] = 1
                else:
                     print('Error reading data. Please ensure each line of orders.txt starts with the bun type (milk or gluten free), followed by a comma, then the sauce type (tomato, barbecue or none), followed by a comma, then the number of patties (0-3), followed by a comma, then the number of slices of cheese (0-3), followed by a comma, then whether tomato is included (yes or no), followed by a comma, then whether lettuce is included (yes or no), followed by a comma, then whether onion is included (yes or no)')
                     #Error handling if the order.txt format is incorrect
    except FileNotFoundError:
        print('File not found, please provide a valid file path to orders.txt.')
        #Error handling if the file path is correct or the file is in the same directory as the program/working directory
    return stored

# get_price takes an input, ideally the key from the store dictionary and calculates the corresponding price of the order
def get_price(stored_value):
    price = base_price
    if stored_value in stored:
        order_tuple = stored_value
        if 'gluten free' in order_tuple:
                price += 1
        price += sum(1 for item in order_tuple[4:] if item == True) - 1
        if order_tuple[2] > 0:
            price += (order_tuple[2]- 1) * 3 
        if order_tuple[3] > 0:
            price += (order_tuple[3]) - 1
    return price
    
 

#This while loop ensures the user inputs a positive integer for the amount of top burger orders they want to retrieve
valid_input = False
while not valid_input:
    try:
        get_top_burger = int(input('How many of the top burgers would you like to output?: '))
        if get_top_burger > 0:
            valid_input = True
        else:
            print('Input error. Please provide a valid integer greater than 0!')
    except ValueError:
        print('Input error. Please provide a valid integer!')

    
order_counts = convert_to_tuple('orders.txt') 
max_views = len(stored)

#This line ensures that if the user tries to pull more orders than there are available - the maximum orders are pulled to avoid error
if get_top_burger > max_views:
     get_top_burger = max_views
     print(f'The amount of unique orders is {max_views}. Here are the top {max_views} orders: ')
#This for loop takes the input number and calls the most occuring order in stored dictionary and then removes that order.
for x in range(get_top_burger):
     max_key = max(stored, key=stored.get)
     print(f"Order: {max_key} Count: {stored[max_key]} Price: ${get_price(max_key)}")
     stored.pop(max_key)






