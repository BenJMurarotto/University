import tkinter as tk
from tkinter import ttk

# Created a burger object with properties that align with Codetown burger options
class Burger:
    def __init__(burger, name, bun, sauce, patties, cheese, tomato, lettuce, onion):
        burger.name = name
        burger.bun = bun
        burger.sauce = sauce
        burger.patties = patties
        burger.cheese = cheese
        burger.tomato = tomato
        burger.lettuce = lettuce
        burger.onion = onion

    # Created a function to calculate the currently selected burger's price when called
    def get_price(burger):
        price = 5  # Base price
        true_count = 0
        if burger.bun == 'Gluten free bun':
            price += 1  # Additional cost for gluten-free bun
        if burger.patties > 1:
            price += (burger.patties - 1) * 3  # Additional cost for extra patties
        if burger.cheese > 1:
            price += (burger.cheese - 1)  # Additional cost for extra cheese
        for item in vars(burger).values():
            if isinstance(item, bool) and item:
                true_count += 1
        if true_count > 1:
            price += (true_count - 1)
        
        return price  # Return the final price


class BurgerMenu:
    def __init__(menu, root):
        menu.root = root
        menu.root.title("Welcome to Codetown Burger Co")

        # List of Codetown burgers converted to objects using class Burger
        menu.burgers = [
            Burger("Byte Burger!", "Milk bun", "Tomato sauce", 1, 0, True, True, False),
            Burger("Ctrl-Alt-Delicious!", "Milk bun", "Barbecue sauce", 2, 2, True, True, True),
            Burger("Data Crunch!", "Gluten free bun", "Tomato sauce", 0, 0, True, True, True),
            Burger("Code Cruncher!", "Milk bun", "Tomato sauce", 3, 3, True, True, True)
        ]
        menu.current_index = 0 

        menu.create_widgets()  # Create UI widgets
        menu.root.after(100, menu.show_burger, menu.current_index)  # Delay initial display to ensure proper alignment
        menu.auto_switch()  # Start automatic cycling of burgers

    # This function provides aesthetic design for the widget set
    def create_widgets(widget):
        widget.frame = ttk.Frame(widget.root)
        widget.frame.pack(padx=500, pady=250, fill='both')

        widget.heading_canvas = tk.Canvas(widget.frame, height=50)
        widget.heading_canvas.pack(fill='x')
        widget.heading = widget.heading_canvas.create_text(75, 0, anchor = 'nw', font = ("Arial", 24))

        widget.menu = ttk.Label(widget.frame, text="", font=("Arial", 16), justify="left")
        widget.menu.pack()

        widget.buttons_frame = ttk.Frame(widget.frame)
        widget.buttons_frame.pack(fill = 'both')

        # Create a button for each burger type
        for index, burger in enumerate(widget.burgers):
            button = ttk.Button(widget.buttons_frame, text = burger.name, command = lambda i = index: widget.click(i))
            button.pack(side = 'bottom', expand = True, fill = 'both')

    # Display the menu items of the selected burger
    def show_burger(line, index):
        burger = line.burgers[index]
        line.heading_canvas.itemconfig(line.heading, text=burger.name)
   

        # Provies a string for burger details
        menu = (
            f"Bun type: {burger.bun}\n"
            f"Sauce type: {burger.sauce}\n"
            f"Number of patties: {burger.patties}\n"
            f"Number of slices of cheese: {burger.cheese}\n"
            f"Tomato included: {'Yes' if burger.tomato else 'No'}\n"
            f"Lettuce included: {'Yes' if burger.lettuce else 'No'}\n"
            f"Onion included: {'Yes' if burger.onion else 'No'}\n"
            f"Price: ${burger.get_price():.2f}"
        )
        line.menu.config(text = menu)  # Updates the menu current with burger details


    # Handle button click to show the selected burger
    def click(click, index):
        click.current_index = index
        click.show_burger(index)
        click.root.after_cancel(click.switch_id)  # Cancel the current auto-switch
        click.auto_switch()  # Restart auto-switch timer

    # Function to automatically switches burgers every 5 seconds
    def auto_switch(self):
        self.switch_id = self.root.after(5000, self.next_burger)

    # Show the next burger on the menu
    def next_burger(self):
        self.current_index = (self.current_index + 1) % len(self.burgers)  # Update index to next burger
        self.show_burger(self.current_index)  # Show the next burger
        self.auto_switch() 

if __name__ == "__main__":
    root = tk.Tk()
    menu = BurgerMenu(root)
    root.mainloop()
