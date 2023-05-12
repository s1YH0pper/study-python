def isometric_strings(a: str, b: str) -> bool:
    dic = {}
    for ind, char in enumerate(a):
        dic[char] = dic.get(char, set()).union(set(b[ind]))
        if len(dic[char]) > 1:
            return False
    return True


print("Example:")
print(isometric_strings("add", "egg"))

# These "asserts" are used for self-checking
assert isometric_strings("add", "egg") == True
assert isometric_strings("foo", "bar") == False
assert isometric_strings("bar", "foo") == True
assert isometric_strings("", "") == True
assert isometric_strings("all", "all") == True
assert isometric_strings("gogopy", "doodle") == False
assert isometric_strings("abba", "cccc") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
