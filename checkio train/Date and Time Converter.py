import time


def date_time(Time: str) -> str:
    t = time.strptime(Time, "%d.%m.%Y %H:%M")
    h = "" if t.tm_hour == 1 else "s"
    m = "" if t.tm_min == 1 else "s"
    return time.strftime(
        f"{t.tm_mday} %B %Y year {t.tm_hour} hour{h} {t.tm_min} minute{m}", t
    )


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"

print("The mission is done! Click 'Check Solution' to earn rewards!")
