def time_converter(time: str) -> str:
    time_list = time.split(sep=":")
    hour = int(time_list[0])
    than_midday = 'p.m.' if hour >= 12 else 'a.m.'
    
    if hour == 0:
        hour = 12
    elif hour > 12:
        hour -= 12

    return f"{hour}:{time_list[1]} {than_midday}"


print("Example:")
print(time_converter("12:30"))
print(time_converter("09:00"))
print(time_converter("23:15"))
print(time_converter('00:00'))

assert time_converter("12:30") == "12:30 p.m."
assert time_converter("09:00") == "9:00 a.m."

print("The mission is done! Click 'Check Solution' to earn rewards!")
