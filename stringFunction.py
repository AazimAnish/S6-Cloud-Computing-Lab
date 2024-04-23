while True:
    
    n = int (input("Enter 1) reverse \n 2) concatinate \n 3) slice \n 4) quit \n"))
    
    if n == 4:
        break
    
    match n:
        case 1:
            revString = input("Enter the string: ")
            print("Reversed string: ",revString[::-1])
            
        case 2:
            string1 = input("Enter the first string: ")
            string2 = input("Enter the second string: ")
            print("Concatinated string: ",string1 + string2 )
        
        case 3:
            string = input("Enter the string: ")
            start = int(input("Enter the starting index: "))
            end = int(input("Enter the ending index: "))
            print("Sliced string: ",string[start:end])
