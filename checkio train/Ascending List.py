def is_ascending(items: list[int]) -> bool:
    if items:
        i = 0
        while i < len(items) - 1:
            if items[i] >= items[i + 1]:
                return False
            i += 1
        return True
    else:
        return True


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
