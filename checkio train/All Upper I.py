def is_all_upper(text: str) -> bool:
    if text and not text.isspace():
        text_list = text.split()
        for i in text_list:
            if i.isdigit() or i.isspace():
                return True
            else:
                text_upper = text.upper()
            return text_upper == text
    else:
        return True


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
