from collections import Counter

sample_text = str(input ('Input text: '))

count = Counter(sample_text)

print(f"{input}: {count}")
