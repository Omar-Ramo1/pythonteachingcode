def fishstore (fish, price):
    return ' Fish type: ' + fish + ' cost $' + price

fish_entry = input('Enter fish type')
price_entry = input('Enter price of fish')

Report = fishstore(fish_entry, price_entry)

print('Report for Omar Idris.' + Report) 