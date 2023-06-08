def checkio(line1: str, line2: str) -> str:
    line1_set = set(line1.split(","))
    line2_set = set(line2.split(","))
    return ",".join(sorted(line1_set & line2_set))


print("Example:")
print(checkio("hello,world", "hello,earth"))

assert checkio("hello,world", "hello,earth") == "hello"
assert checkio("one,two,three", "four,five,six") == ""
assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

print("The mission is done! Click 'Check Solution' to earn rewards!")
