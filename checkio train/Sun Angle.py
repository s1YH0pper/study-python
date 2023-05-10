from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    h, m = map(int, time.split(":"))
    angle = h * 15 + m * 0.25 - 90
    if 0 <= angle <= 180:
        return angle
    else:
        return "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")
