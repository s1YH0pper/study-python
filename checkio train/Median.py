def checkio(data: list[int]) -> int | float:
    items = sorted(data)
    if len(items) % 2 == 0:
        result = (items[len(items) // 2 - 1] + items[-(len(items) // 2)]) / 2
    else:
        result = items[len(items) // 2]
    return result


print("Example:")
print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

print("The mission is done! Click 'Check Solution' to earn rewards!")
