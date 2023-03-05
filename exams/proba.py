def shopping_cart(*args):
    limits = {'Pizza': 4, 'Dessert': 2, 'Soup': 3}
    menu = {'Pizza': set(), 'Dessert': set(), 'Soup': set()}
    for el in args:

        if el != 'Stop':
            meal = el[0]
            product = el[1]
            if meal in menu:
                if len(menu[meal]) < limits[meal]:
                    menu[meal].add(product)
        else:
            break
    final = sorted(menu.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for i in final:
        main, product = i
        result += main + ':' + "\n"
        for p in product:
            result += " - " + p + "\n"
    if any(menu.values()):
        return result
    else:
        return "No products in the cart!"

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
