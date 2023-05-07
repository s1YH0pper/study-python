def nearest_value(values: set[int], one: int) -> int:
    min_dist, closest_num = None, None
    for value in values:
        dist = abs(one - value)
        if min_dist is None or min_dist > dist:
            min_dist, closest_num = dist, value
        elif min_dist == dist:
            closest_num = min(value, closest_num)

    return closest_num


print("Example:")
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
