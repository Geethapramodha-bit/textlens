import string

text = input()

formatted_text = text.lower().split()
total = len(formatted_text)

frequency = {}

for word in formatted_text:
    cleaned = word.strip(string.punctuation)

    if cleaned in frequency:
        frequency[cleaned] += 1
    else:
        frequency[cleaned] = 1

count = 0

for char in text:
    if char == "." or char == "!" or char == "?":
        count += 1

print("Sentences:", count)
print("Frequency:", frequency)
print("Total words:", total)
print("Unique words:", len(frequency))