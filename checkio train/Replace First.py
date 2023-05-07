from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    if not items:
        return items
    else:
        a = items.pop(0)
        items.append(a)
        return items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
