# Open the text file for reading
with open("level2/myfile.txt",'r' )as file:
    text = file.read()

# Remove punctuation and convert to lowercase
text = text.lower()
text = ''.join([c for c in text if c.isalnum() or c.isspace()])

# Split the text into words
words = text.split()

# Create a dictionary to store word counts
word_counts = {}

# Count the occurrences of each word
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort the dictionary by keys (words) in alphabetical order
sorted_word_counts = dict(sorted(word_counts.items()))

# Display the results
for word, count in sorted_word_counts.items():
    print(f"{word}: {count}")