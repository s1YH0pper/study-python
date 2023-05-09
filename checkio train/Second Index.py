def second_index(text: str, symbol: str) -> [int, None]:
    """
    returns the second index of a symbol in a given text
    """
    if text.count(symbol) < 2:
        return None
    else:
        first = text.find(symbol)
        second = text.find(symbol, first + 1)
    return second


print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
