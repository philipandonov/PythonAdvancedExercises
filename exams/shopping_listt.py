def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    number_of_products = 0
    str_to_print = ''
    for key, value in kwargs.items():
        if number_of_products == 5:
            break
        total_price = value[0] * value[1]
        if total_price <= budget:
            number_of_products += 1
            str_to_print += f"You bought {key} for {total_price:.2f} leva." + "\n"

    return str_to_print


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

