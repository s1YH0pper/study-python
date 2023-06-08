from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    result = sorted(numbers, key=lambda i: (-numbers.count(i), i))
    return result


print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
