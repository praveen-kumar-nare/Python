s = "sometimes pains but necessary are changes"


def reverse_words(words):
    if not words:
        return ""
    return words[-1] + " " + reverse_words(words[:-1])


reversed_words = reverse_words(s.split()).strip()

print(reversed_words)