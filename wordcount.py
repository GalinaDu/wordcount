"""Count words in file."""
import sys

input_file = open(sys.argv[1])

words_count = {}

for line in input_file:
    line = line.rstrip()

    words = line.split()

    for word in words:
        words_count[word] = words_count.get(word, 0) + 1

for word, count in words_count.items():
    print(word, count)


