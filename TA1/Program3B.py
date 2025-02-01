#Program3B

# outer loop for the starting number of rows
row = 1

while row <= 7:
    if row == 2 or row == 4:
        row += 1  # Increment the row before skipping
        continue  # Skip the current row
    
    # Initialize the inner loop for printing numbers
    count = 0 #initialize the number of digit to be printed in each row to 0
    while count < row:
        print(row, end="")
        count += 1 #Increment count by 1 each iteration; it resets to 0 after the loop ends
    print()  # Move to the next line
    row += 1 
