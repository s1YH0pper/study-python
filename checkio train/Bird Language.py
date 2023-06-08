def translate(text: str) -> str:
    vowels_letters = "aeiouy"
    text_list = text.split()
    translated_words = []
    
    for text in text_list:
        translated_word = ""
        i = 0
        while i < len(text):
            translated_word += text[i]
            if text[i] in vowels_letters:
                i += 3
            elif text[i] not in vowels_letters:
                i += 2
            else:
                i += 1

        translated_words.append(translated_word)
    
    translated_phrase = " ".join(translated_words)
    return translated_phrase


print("Example:")
print(translate("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translate("hieeelalaooo") == "hello"
assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translate("aaa bo cy da eee fe") == "a b c d e f"
assert translate("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")
