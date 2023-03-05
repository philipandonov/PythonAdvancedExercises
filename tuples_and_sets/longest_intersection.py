n = int(input())
intersections = []
for _ in range(n):
    first_range, second_range = input().split('-')
    start, stop = [int(el) for el in first_range.split(',')]
    first_set = range(start, stop+1)

    start, stop = [int(el) for el in second_range.split(',')]
    second_set = range(start, stop+1)
    intersection = set(first_set).intersection(second_set)
    intersections.append(intersection)

longest_intersection = sorted(intersections, key=lambda x: -len(x))

longest_intersection_list = [x for x in longest_intersection[0]]
print(f"Longest intersection is {longest_intersection_list} with length {len(longest_intersection[0])}")