exclude_words = ["and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"]

user_input = input("Enter a string statement: ")
print('')

words = user_input.split()  # Separates statement into individual words
count = {}  # Store number of words
lowercase = []
uppercase = []

for word in words:
    word_fixed = word.strip(",.!?")  # Remove punctuation but keep the original case
    word_lower = word_fixed.lower()  # Convert to lowercase for checking

    if word_lower.isalnum():
        if word_lower not in exclude_words:  # Check if it's not in excluded words
            count[word_fixed] = count.get(word_fixed, 0) + 1  # Store original word

#separate words into lowercase and uppercase categories
for word in count:
    if word[0].islower():
        lowercase.append(word)
    else:
        uppercase.append(word)

#to sort in alphabetical order
lowercase.sort()
uppercase.sort()

if count:
    max_length = max(len(word) for word in count)  
else:
    max_length = 0

for word in lowercase:
    print(word.ljust(max_length + 2) + "- " + str(count[word]))  # ljust for alignment
for word in uppercase:
    print(word.ljust(max_length + 2) + "- " + str(count[word]))

print("\nTotal words filtered:", sum(count.values()))
