# Taken from mission Acceptable Password II


# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        for word in password:
            if word.isalpha():
                for i in password:
                    if i.isdigit():
                        return True
                return False
            else:
                return False
    else:
        return False


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
