from typing import Iterable


def replace_last(line: list) -> Iterable:
    if line:
        replace = line.pop()
        line.insert(0, replace)
        return line
    return line


print("Example:")
print(list(replace_last([2, 3, 4, 1])))

assert list(replace_last([2, 3, 4, 1])) == [1, 2, 3, 4]
assert list(replace_last([1, 2, 3, 4])) == [4, 1, 2, 3]
assert list(replace_last([1])) == [1]
assert list(replace_last([])) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
