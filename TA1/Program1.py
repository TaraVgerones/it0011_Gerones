#Counting vowels, consonants and spaces in a string

#prompt user to input a string
Text = input('Enter a String: ')

#Initializing variables for vowels and consonants
vowels = 'aAeEiIoOuU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'

#initializing count variables to 0 
vowel_count = consonants_count = space_count = others_count = 0

#Loop to traverse alphabet 
for alphabet in Text:
    if alphabet in vowels:
        vowel_count += 1
    elif alphabet in consonants:
        consonants_count +=1
    elif alphabet == ' ':
        space_count += 1
    else:
        others_count += 1
        
#Print the Output
print() #new line
print('Number of Vowels: ', vowel_count)
print('Number of Consonants: ', consonants_count)
print('Number of Spaces: ', space_count)
print('Other Characters: ', others_count)