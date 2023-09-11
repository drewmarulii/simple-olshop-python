def print_malls():
    print('List of Malls')
    print('1) Kota Kasablanka')
    print('2) Ambassador')
    print('3) Pejaten Village')
    print('4) Kemang Village')

def choose_mall():
    mall = input('Choose Mall: ')
    return int(mall)

def mall_name(mall_number):
    if mall_number == 1:
        mall_name = 'Kota Kasablanka'
    elif mall_number == 2:
        mall_name = 'Ambassador'
    elif mall_number == 3:
        mall_name = 'Pejaten Village'
    elif mall_number == 4:
        mall_name = 'Kemang Village'
    else:
        print('Unknown Mall, Try again!')
    return mall_name

def print_products():
    print('\nList of Products')
    print('1) Clothes')
    print('2) Electronic')

def choose_product():
    product = input('Choose Product: ')
    return int(product)
    
def product_name(product_number):
    if product_number == 1:
        product_name = 'Clothes'
    elif product_number == 2:
        product_name = 'Electronic'
    else:
        print('Unknown Input, Try again!')
    return product_name

def set_quantity():
    quantity = input('Quantity: ')
    return int(quantity)

def calculate(mall_number, product_number, qty):
    clothes = 100000
    electronic = 500000

    if product_number == 1:
        sub_total = clothes * qty
        if mall_number == 1:
            discount = 0.2 * sub_total
        elif mall_number == 2:
            discount = 0.15 * sub_total
        elif mall_number == 3:
            if qty == 1:
                discount = 0.05 * sub_total
            elif qty >1:
                discount = 0.2 * sub_total
    elif product_number == 2:
        sub_total = electronic * qty
        if mall_number == 1:
            discount = 0.1 * sub_total
        elif mall_number == 2:
            discount = 0.25 * sub_total
        elif mall_number == 3:
            discount = 0.3 * sub_total
        elif mall_number == 4:
            discount = 0.15 * sub_total

    total_price = sub_total - discount
    return total_price

def order_again():
    print('\nOrder Again?')
    print('1) Yes')
    print('2) No')
    choose = input('Choose Number: ')

    if choose == '1':
        print('\n')
        start()
    elif choose == '2':
        print('Thank you!')

def order_summary(totalprice, mall, item, qty):
    print('\nOrder summary: ')
    print(f"You have bought {qty}X {item} with Total Price Rp {totalprice} from {mall} Mall")

def start():
    print_malls()
    mall_number = choose_mall()
    print_products()
    product_number = choose_product()
    product_name(product_number)
    mall = mall_name(mall_number)
    item = product_name(product_number)
    qty = set_quantity()
    totalprice = calculate(mall_number, product_number, qty)
    order_summary(totalprice, mall, item, qty)
    order_again()
start()