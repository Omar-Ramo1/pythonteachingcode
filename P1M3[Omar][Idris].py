def cheese_order(order_amount, min=1.0, max=100.0, price=7.99):
    maximum = float(max)
    minimum = float(min)
    price = float(price)
    order_amount = float(order_amount) 

    if order_amount > maximum:
        print(str(order_amount) + ' is more than currently available stock')

    elif order_amount < minimum:
        print(str(order_amount) + 'is below minimum order amount')

    else:
        total_cost = order_amount * price 
        print(str(order_amount) + ' cost $' + str(total_cost))

user_input = input("Omar Idris, enter cheese order weight (numeric value): ")
cheese_order(user_input)