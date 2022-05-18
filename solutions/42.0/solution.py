def search(text, word):
    if word in text:
        return "Word found"
    return "Word not found"

text = input()
word = input()

print(search(text, word))