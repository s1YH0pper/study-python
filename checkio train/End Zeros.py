def end_zeros(a: int) -> int:
    text = str(a)
    text_length = len(text)
    text_length_without_zero = len(text.strip('0'))
    return text_length - text_length_without_zero


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
