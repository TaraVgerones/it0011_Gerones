#Getting the sum of the digits from a given input string digits

# Prompt user input
digit = input('Enter a String with Number(s): ')

# Initialize sum variable
digit_Total = 0

# Loop through each character in the string
for char in digit:
    # Check if the character is a digit by comparing if it's between '0' and '9'
    if '0' <= char <= '9':
        # Convert character to integer and add the value to 'total'
        digit_Total += int(char)

# Print the Output
print('Sum of the digits in your string:', digit_Total)

    