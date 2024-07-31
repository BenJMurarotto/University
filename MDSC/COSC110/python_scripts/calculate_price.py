def calculate_price(price, order):
    cost = 0
    
    for item in order:
        
            if item in price:
                cost += price[item]*order[item]
            else:
                raise KeyError('Item not valid')
        
    if cost > 100:
        final_cost = cost - 0.1*cost
    elif cost > 50:
        final_cost = cost - 0.05*cost
    else:
         final_cost = cost

    print(f'Final cost comes to ${final_cost:.2f}')

price = {'Table' : 50, 'Chair' : 30, 'Fridge' : 400}
order = {'Fridge' : 400}

calculate_price(price, order)