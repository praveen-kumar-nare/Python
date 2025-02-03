s = "praveen kumar"
words = s.split()


reversed_words = ""


for word in reversed(words):
    reversed_words += word + " "


reversed_words = reversed_words.strip()

print(reversed_words)