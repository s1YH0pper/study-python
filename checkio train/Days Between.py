def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    from datetime import date, timedelta
    return abs((date(a[0], a[1], a[2]) - date(b[0], b[1], b[2])).days)


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

print("The mission is done! Click 'Check Solution' to earn rewards!")
