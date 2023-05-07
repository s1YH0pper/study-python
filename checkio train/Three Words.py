def checkio(words: str) -> bool:
    count = 0
    if len(words.split()) >= 3:
        for i in words.split():
            if i.isalpha():
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
