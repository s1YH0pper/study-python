def is_majority(items: list[bool]) -> bool:
    count_t = 0
    count_f = 0
    for i in items:
        if bool(i):
            count_t += 1
        else:
            count_f += 1

    if count_t > count_f:
        return True

    return False


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
