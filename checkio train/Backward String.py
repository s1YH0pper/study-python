def backward_string(val: str) -> str:
    reverse_val = val[::-1]
    return reverse_val


print("Example:")
print(backward_string("val"))

# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")
