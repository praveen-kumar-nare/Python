
s = "my tongue is my enemy"


words = s.split()


stack = []
for word in words:
    stack.append(word)

reversed_words = ""
while stack:
    reversed_words += stack.pop() + " "


reversed_words = reversed_words.strip()

print(reversed_words)