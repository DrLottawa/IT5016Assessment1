#Before we start anything, first we import the modules and libraries that we will need. In this case the floor method from the math module so that we may round down the scores of the
#player later on as well as the random module so that we can pick a random number for the player to try and guess via the randint method
from math import floor
import random

#Here we define a function labelled GetAnswer. This takes in the parameter of prompt.The purpose of this method is to get the input of the user can convert it into an integer, returning
#it if successful and returning null otherwise
def GetAnswer(prompt):
    #This is a try except block that will house the converting method in its try method. If it fails (ie, a non numerical character is input) the program will move on to the except
    #block instead of crashing. Here in this except block we simply return the method with a null value. This way we can elegantly handle any errors that arise. Otherwise the input
    #string we be returned as a integer
    #Documentation on try/except blocks: https://www.w3schools.com/python/python_try_except.asp
    try:
        #Here the prompt which was passed into the method will displayed to the user where they may input their answers.
        #Documentation on functions and returning: https://www.w3schools.com/python/python_functions.asp
        return int(input(prompt))
    except:
        return

#This is the function where the game itself is decleared. Calling this function will begin the game.
def game_start():
    #Here we set a boolean labeled retry. We will use this with a while loop to let the user choose if they want to retry the game or not. At initialisation we set it to true
    retry = True
    #Here we check the retry bool. If it is true we will start the game. Initally this will always be set to true so we can actually begin the game at all. Later on in the game
    #the user will get to change this if they dont want to play anymore
    while(retry):
        #These two variables will be used for giving the user a score. Starting at 200 the score will lose an amount of points every turn they dont guess the number equal to their
        #current score divided by the divider which is incremented every additional turn. Formula: score = (score - (score/(2 + n))) where n = number of previous guesses
        score = 200
        divider = 2

        #At this point the computer will call the randint method and return a integer between 1 and 100. This number will be stored in a variable ai_choice and will be used as the number
        #for the player to try and guess.
        ai_choice = random.randint(1, 100)
        #Here we store each answer the player made. This will be used for two purposes, one to check the users last number guessed so that we may determine if it is closer or further
        #than their current answer and secondly so that we can get a tally on how many guesses it took them to guess the answer.
        last_answer = []
        #This is our first call to the GetAnswer method where we initally prompt the user for a number between 1 and 100 and assign what it returns to the current_answer variable
        current_answer = GetAnswer("I've thought up a number between 1 and 100. Can you guess what it is?\n")
        #and here we make sure that GetAnswer actually returned a value. If not the program will hit the continue keywords and restart the while loop. This will continue until an
        #integer is returned.
        if current_answer is None:
            continue

        #This is the while loop we use to continue the game until the answer is guessed. The program will loop back here after each guess and check if the current_answer variable is
        #equal to the number chosen by the computer. If not it will move on to display if the player is hot or cold then prompt them for the next answer
        while(current_answer != ai_choice):
            #This prompt variable contains the string "Colder...". This is what the default message is that will be displayed to the player and will only be changed if it is the inital
            #guess or if the guess is close to the answer.
            prompt = "Colder...\n"
            #In this if statement we check the last_variable list to see if it has any items. If not then its safe to assume that the player is making their first guess and so do not have
            #a previous answer to compare the current_answer to. We also check to see if they have entered the same answer they previously did otherwise. In this case we display the same
            #message
            if last_answer.__len__() == 0 or current_answer == last_answer[-1]:
                prompt = "Nope! Try again.\n"
                
            #And in the case it doesnt meet either of those conditions we then check if it is closer. To do this we create and array containing two items. The difference between the ai_choice
            #and the current answer and the difference between the last answer answer given (obtained by indexing -1 from the array of previous guess which returns the last item). These are
            #converted to their absolute values for the sake of consistantcy using the abs() method. We then use the min() method to get the lower one of these two numbers. This value will be
            #the closer number to the answer. From their we do a comparison to see if this is equal to the current guess difference. If it is then the current guess is closer to the answer and
            #thus we change the prompt to inform the player that they are warmer to the ai_choice.
            #Documentaion on abs(): https://www.w3schools.com/python/ref_func_abs.asp
            #and min(): https://www.w3schools.com/python/ref_func_min.asp
            elif min([abs(ai_choice - current_answer), abs(ai_choice - last_answer[-1])]) == abs(ai_choice - current_answer):
                prompt = "Warmer...\n"

            #Once the prompt is obtained we will then recalculate the score. This is done by dividing the current score by the divider and then taking that off of the current score
            #which starts at a default of 2. Once this is done we use the floor() method to round it down in case it comes back as a float. After thats finished we take the divider
            #increment it by 1. This way the next time we come around to these two methods the amount of score taken off is less than before. Doing this grants exponentially more points
            #for getting the answer sooner and makes repeated failed guesses less harsh.
            #Documentation on python shorthand operators: https://www.w3resource.com/python/python-operators.php
            score -= floor(score/divider)
            divider += 1

            #And then here we append the current_answer variable to the last_answer array. This way it can be used for the next comparison if it comes around and be counted in the tally
            #of guesses
            last_answer.append(current_answer)
            #Finally we call the GetAnswer method once more with the prompt we assigned earlier based on our calculated comparisons and get the next guess from the user to compare.
            current_answer = GetAnswer(prompt)
            
        #Once we get to this point the answer has been successfully guessed and the user is congratulated. We display the score and the amount of guesses taken using the s% string formatting
        #and ask the user if they would like to retry. If the user inputs one of the accepted input strings the continue keyword will be hit and the game restarted at the top of the loop.
        #Otherwise the retry variable is set to false, the while loop is satisfied and end of game message is displayed.
        retry_prompt = input("Congratulations, you won!\nYour score was %s\n\nYou made %s guesses.\n\nWould you like to play again? \n\n" %(score, len(last_answer + 1)))
        if(['yes', 'y', '1', 'true', 'ok', 'sure', 'yeah'].__contains__(retry_prompt.lower())):
            continue
        retry = False


    input("========================\nThanks for playing!\n========================\nPress Enter to quit")

#Then here we call the game_start method which calls the game function in the first place.
game_start()

