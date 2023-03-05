def shopping_cart(*args):
    products = {'Soup': [], 'Pizza': [], 'Dessert': []}

    for product in args:
        is_same = False
        if product == "Stop":
            break
        for value in products.values():
            if product[1] in value:
                is_same = True
        if is_same:
            continue
        if len(products['Soup']) >= 3:
            continue
        if len(products['Pizza']) >= 4:
            continue
        if len(products['Dessert']) >= 2:
            continue
        products[product[0]].append(product[1])

    sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))
    result_str = ''
    for key, value in sorted_products:
        sorted_values = sorted(value)
        result_str += key + ':' + "\n"
        for val in sorted_values:
            result_str += " - " + val + "\n"

    if len(products['Soup']) == 0 and len(products['Pizza']) == 0 and len(products['Dessert']) == 0:
        return 'No products in the cart!'
    else:
        return result_str


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

