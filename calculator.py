while True:

    n = input("Enter 1) + for addition, \n 2) - for substraction, \n 3) * for multiplication, \n 4) / for division, \n 5) q to quit \n")
    a = int (input("Enter first number: "))
    b = int (input("Enter second number: "))
    
    if n == 'q':
        break

    match n:
        case "+":
            print("a + b = ",a+b)
            
        case "-":
            print("a - b = ",a-b)
            
        case "*":
            print("a * b = ",a*b)
        
        case "/":
            print("a / b = ",a/b)
        
        case _:
            print("Invalid operation try agian!")
        