def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0

    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    return text[begin_index:end_index]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
