def division(): #division function
    print(" DIVISION ".center(40, '-'))
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    
    if num2 == 0: #Error 
        print("-" * 40)
        print("Try Again! The second number cannot be zero.")
        return None
    else:
        answer = num1 / num2 #equation
        print(f"Answer: {answer:.2f}")
        return answer

def exponentiate(): #exponentiation function
    print(" EXPONENTIATION ".center(40, '-'))
    base = int(input("Enter Base Number: "))
    exponent = int(input("Enter Exponent Number: "))
    
    answer = base ** exponent #equation
    print("Answer: ",answer)
    return answer
    
def remainder(): #remainder function 
    print(" REMAINDER ".center(40, '-'))
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    
    if num2 == 0: #Error
        print("-" * 40)
        print("Try Again! The second number cannot be zero.")
        return None
    else:
        answer = num1 % num2 #equation - used modulo
        print("Answer: ",answer)
        return answer

def summation(): #summation function
    print(" SUMMATION ".center(40, '-'))
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    
    if num1 > num2: #Error
        print("-" * 40)
        print("The second number must be greater than the first number.")
        return None
    else:
        answer = sum(range(num1, num2 + 1)) #equation
        print("Answer: ",answer)
        return answer
    
#main menu function
while True:
    print("=" * 40)
    print(" MATHEMATICAL OPERATIONS MENU ".center(40, '='))
    print("[D]. Divide")
    print("[E]. Exponentiation")
    print("[R]. Remainder")
    print("[F]. Summation")
    print("[X]. Exit")
    print("=" * 40)
        
    choice = input("Enter your choice: ").strip().upper() #convert the user input to uppercase
    print("-" * 40)
    
    if choice == 'D': 
        division()
    elif choice == "E":
        exponentiate()
    elif choice == "R":
        remainder()
    elif choice == "F":
        summation()
    elif choice == "X": 
        print("Thank you! Have a nice day.")
        print("-" * 40)
        break
    else:
        print("Invalid Choice. Try Again!")
        
        