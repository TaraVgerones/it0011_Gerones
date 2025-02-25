file = open("C:\Users\Tara Gerones\Documents\GitHub\it0011_Gerones\TME", 'r') 
lines = file.readlines()

for i, line in enumerate(lines, start = 1):
    numbers = list(map(int, line.strip().split(',')))
    total = sum(numbers)
    if str(total) == str(total)[::-1]:
        result = "Palindrome"
    else:
        result = "Not a palindrome"
    print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")