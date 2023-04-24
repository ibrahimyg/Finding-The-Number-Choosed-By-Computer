import random

def guessGame(x):
    chosenNumber = random.randint(1,x)
    if 100 >= x >= 1:
        for i in range(10):
            guess = int(input(f"Please enter a number between 1 and {x}"))                  
            if guess > chosenNumber + 25: 
                print("The number entered is too big")
            elif guess + 25 < chosenNumber:
                print("The number entered is too small")
            elif guess > chosenNumber:
                print("The number you entered is big")
            elif guess < chosenNumber:
                print("The number you entered is small")  
            elif guess == chosenNumber:
                print("You guessed correctly!")
                break
            if guess != chosenNumber:
                print("You got it wrong! The number was "+ " " + str(chosenNumber) )
                
    if 350 >= x > 100:                      
        for i in range(10):    
            guess = int(input(f"Please enter a number between 1 and {x}"))   
            if guess > chosenNumber + 50:
                print("The number entered is too big")
            elif guess + 50 < chosenNumber:
                print("The number entered is too small")
            elif guess > chosenNumber:
                print("The number you entered is big")
            elif guess < chosenNumber:
                print("The number you entered is small")
            elif guess == chosenNumber:
                print("You guessed correctly!")
                break
        if guess != chosenNumber:
            print("You got it wrong! The number was "+ " " + str(chosenNumber) )
            
    if 1000 >= x > 350:    
        for i in range(10):            
            guess = int(input(f"Please enter a number between 1 and {x}"))   
            if guess > chosenNumber + 250:
                print("The number entered is too big")
            elif guess + 250 < chosenNumber:
                print("The number entered is too small")
            elif guess > chosenNumber:
                print("The number you entered is big")
            elif guess < chosenNumber:
                print("The number you entered is small")
            elif guess == chosenNumber:
                print("You guessed correctly!")
                break
        if guess != chosenNumber:
            print("You got it wrong! The number was "+ " " + str(chosenNumber) )
            
    if 5000 >= x > 1000:    
        for i in range(10):             
            guess = int(input(f"Please enter a number between 1 and {x}"))   
            if guess > chosenNumber + 500:
                print("The number entered is too big")
            elif guess + 500 < chosenNumber:
                print("The number entered is too small")
            elif guess > chosenNumber:
                print("The number you entered is big")
            elif guess < chosenNumber:
                print("The number you entered is small")
            elif guess == chosenNumber:
                print("You guessed correctly!")
                break
        if guess != chosenNumber:
            print("You got it wrong! The number was "+ " " + str(chosenNumber) )
            
    if 10000 >= x > 5000:    
        for i in range(10):                
            guess = int(input(f"Please enter a number between 1 and {x}"))   
            if guess > chosenNumber + 1000:
                print("The number entered is too big")
            elif guess + 1000 < chosenNumber:
                print("The number entered is too small")
            elif guess > chosenNumber:
                print("The number you entered is big")
            elif guess < chosenNumber:
                print("The number you entered is small")
            elif guess == chosenNumber:
                print("You guessed correctly!")
                break
        if guess != chosenNumber:
            print("You got it wrong! The number was "+ " " + str(chosenNumber) )
                    
guessGame(int(input("Please input a number!")))  
               
