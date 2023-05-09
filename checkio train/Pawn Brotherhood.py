def safe_pawns(pawns: set) -> int:
    safe_chess = 0
    pawns_index = []
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_index.append((row, col))
    
    for x, y in pawns_index:
        if ((x - 1),(y - 1)) in pawns_index or ((x - 1),(y + 1)) in pawns_index:
            safe_chess += 1
    return safe_chess


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
