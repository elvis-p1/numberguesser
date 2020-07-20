import random

#Returns a random integer within the range inclusively (start,end)
#start - start of range
#end - end of range
def generate(start,end):
    return random.randint(start,end)

#Number of guesses allowed
guessLimit= 5
#Number of guesses made by the user
guessCount = 0

#Reset the variables to run the program again
def reset():
    global a,b,guessCount,endRec,startRec
    a = 0
    b = 0
    guessCount = 0
    startRec = False
    endRec = False

#Are true when the start and end numbers for the range are received
startRec = False
endRec = False

#a - start of range
#b - end of range (inclusive)
a = 0
b = 0

#A prompt message
print("Give the starting and ending number, separate by space.")
print("e.g. 3 60")

#Main program loop
running = True
while running:

    #Prompt message and receiving user's range
    print("The first two numbers in your input will be used for the range")
    string = input("")

    #Get a string list of the input
    list = string.split(" ")
    for temp in list:
        try:
            temp = int(temp)
            if not startRec:
                startRec = True
                a = temp
            elif not endRec:
                endRec = True
                b = temp
            else:
                break     
        #Skip values that cannot be converted to int
        except ValueError:
            continue
    
    #Two integers were not found, or the end of the range is larger than the start (invalid)
    if not startRec or not endRec or a > b:
        print("The two numbers from your input were not found or the range is not proper")
        print("Improper input. Enter N to quit or enter anything else to retry")

    #Two integers have been recorded
    elif startRec and endRec:
        #Generating a random number within the given range
        hidden = generate(a,b)
        #Tell the user the range it is in
        guess = int(input("Guess the number. It is between " + str(a) + " and " + str(b) + " "))

        #The user gets a limited amount of guesses
        #Each guess increases a counter
        #If the counter exceeds the limit or the user guesses correctly
        while guessCount < guessLimit-1:
            guessCount += 1
            #The user guessed wrong
            if guess != hidden:
                if guessLimit-guessCount != 1:
                    #Displays when the user makes a mistake 
                    print("Wrong. You have " + str(guessLimit-guessCount) + " guesses left. Try again:")
                else:
                    #Displays if the user only has one more guess
                    print("Wrong. You have " + str(guessLimit-guessCount) + " guess left. Try again:")
                guess = int(input(""))
            elif guess == hidden and guessCount == 1: 
                #Displays if the user gets it on their first guess
                print("You got it within " + str(guessLimit) + " guess. Not bad!")
                #Stop guessing
                break
            else:
                #Displays if the user does not get it within their first guess
                print("You got it within " + str(guessLimit) + " guesses. Not bad!")
                #Stop guessing
                break
        if guess != hidden and guessCount == guessLimit-1:
            #Displays when the user runs out of guesses
            print("No more guesses. The number was " + str(hidden))
            #A prompt to retry guessing
            print("Enter N to quit or enter anything else to retry")
        else: 
            #Displays when the user gets the correct number
            print("Good job! Enter N to quit or enter anything else to retry")

    #If the user inputs "N" or "n" the program terminates
    #Otherwise, the program runs again 
    rerun = input("")
    if rerun.lower() == "n":
        #Program end message
        print("Program ending...")
        #While loop ends
        running = False  
    else:
        #Reset the variables
        reset()

#Exit
