#Program3A

#outer loop
for i in range (1, 6): #for number of rows (5)
    #1st inner loop 
    for j in range (5 - i):
        print(' ', end='') #for spaces printed before the numbers in each row
    #2nd inner loop
    for j in range (1, i + 1): #starting number is 1 until 4(i) + 1
        print(j, end='') #for numbers that will be printed in each row
    print() #new line 
    


