def sum_positives(*args):
    positive_numbers = [x for x in args if x > 0]
    print(sum(positive_numbers))
    return sum(positive_numbers)


def sum_negatives(*args):
    negative_numbers = [x for x in args if x < 0]
    print(sum(negative_numbers))
    return sum(negative_numbers)


def which_is_great():
    if abs(sum_negatives(*numbers)) > sum_positives(*numbers):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]

which_is_great()
