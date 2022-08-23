#And so here, I've whipped up my own rock paper scissors simulation. It works by having an array containing each possible hand to throw (paper, scissors or rock) and selecting one
#at random. The user is then allowed to select paper, scissors or rock and have compared to the computer. The computer is then able to print out a response indicating if the user
#won or not. It is then able to ask if the player would like to try again or end the game. This too will have an appropriate response.

#First we import the random module which contains the choice method which we will use to get a random item out of our outcome dictionary
import random

#Then we begin to define our game function here
def game_start():
    #In this outcomes variable we pull off a few key things. First we open with curly brackets to declear this variable as a dictionary. A dictionary is a collection of key value pairs.
    #Here we will have 3 key/value pairs with paper, scissors and rock being our keys. In each of these pairs we define the value of each pair as a list of strings. These strings
    #are ordered in a specific manner with the 0 index containing the string that fufills the lose condition for the key's respective string, the 1 index containing the key's value
    #in case of a tie and the 2 index containing the value for the key's win condition.
    outcomes = {'paper' : ['scissors', 'paper', 'rock'], 'scissors' : ['rock', 'scissors', 'paper'], 'rock' : ['paper', 'rock', 'scissors']}
    #Here we set a boolean labeled retry. We will use this with a while loop to let the user choose if they want to retry the game or not. At initialisation we set it to true
    retry = True
    #Here we check the retry bool. If it is true we will start the game. Initally this will always be set to true so we can actually begin the game at all. Later on in the game
    #the user will get to change this if they dont want to play anymore
    while(retry != False):
        #The AI's turn! Here we create a variable of type str. This will call the choice method from the random module and parse a list object which contains our outcomes dictionary
        #as a parameter. Parsing the dictionary into the list returns a list with the keys in the dictionary. Random.choice is then able to pick a random item from the list it is
        #given, in this case the list of key strings. This random item is used as the AI's choice of rock, paper or scissors.
        ai_choice: str = random.choice(list(outcomes))
        #And finally here we ask the user to make their choice of paper, scissors or rock. Here we use the input method to record the string input from the user and save it as the 
        #user_input variable. 
        user_input = input("\n\n(1) Paper \n(2) Scissors \n(3) Rock\n")
        #For the case of consistancy and several ways to type the answer to the previous prompt here we some if statements that take what the user input and check them against a list
        #of possible inputs corresponsing to their respective choices using the __contains__ method. This accomodates multiple answer inputs. The users inputted string is brought 
        #lower case and compared againstour accepted inputs. This is to make sure that regardless of the case it was entered in that it matches the accepted inputs. Then if it is 
        #determined to be an accepted input we transform it into the lower case string for the users answer so we can use it for future comparison. If it doesnt match any of the
        #accepted inputs we simply hit a continue keyword which will bring us back to the beginning of the loop where the user will be asked again for an answer.
        if(['paper', '1', 'a'].__contains__(user_input.lower())):
            user_input = 'paper'
        elif(['scissors', '2', 'b'].__contains__(user_input.lower())):
            user_input = 'scissors'
        elif(['rock', '3', 'c'].__contains__(user_input.lower())):
            user_input = 'rock'
        else:
            continue

        #Finally, once we have the users choice and the AI's choice will will print them both out to the user. Printed out is a statement that utilises the python %-formatting. 
        #%-formatting allows you to apply %s within the string anywhere you like. From there, at the end of the string we can then have brackets in place formatted %() where items
        #we pass through as parameters are added to the string in the order of which they appear so the first item passed is added to the first instance of %s and so on. The items
        #we parse in are also given the .capitalize() method which goes to captilize the first letter of the strings, making things look a little neater
        print('\n\nYou have selected %s. The computer has selected %s' %(user_input.capitalize(), ai_choice.capitalize()))
        #This is where the final choice is made. Here we create a match statement which takes a value as checks each of its cases to which case matches its value. In this case we
        #get the outcome key value corresponding to the choice the AI made. This value is list with a ordered conditions. From there we use the .index() method and parse the
        #user_input variable in to get the index number which equals the users choice. This index number will always corresponding to how it relates the key aka the ai_choice with
        #0 being that it wins, 1 it ties and 2 being it loses. Based on this index we print out the respective decision to the user thus concluding the game of paper scissors rock.
        match outcomes.get(ai_choice).index(user_input):
            case 0:
                print('Congratulations! You won! \n \n')
            case 1:
                print('We have a tie! \n \n')
            case 2:
                print('Oh no, you lost! \n \n')

        #Once the game has been concluded we ask the user if they would like to play the game again with an input. This input utilises the previous method of accepted inputs and 
        #input standardisation. In the case that it does match an accepted input the code will hit the continue keyword and be returned to the top of the while loop where the retry
        #bool will still be true thus starting the game again. Otherwise the retry value is set to false and immediately the while loop will be checked again. The value will be false
        #and so the game will properly end.
        retry_prompt = input("Would you like to play again? \n\n")
        if(['yes', 'y', '1', 'true', 'ok', 'sure', 'yeah'].__contains__(retry_prompt.lower())):
            continue
        retry = False
    
    #Once the game is properly ended the console print out a input displaying thank you for playing and propmt the player to press any key to quit. This is an input so that the window
    #doesnt close itself the moment this line is printed out and only when the user is ready to quit.
    input("========================\nThanks for playing!\n========================\nPress any key to quit")

#And finally. Here we call the game_start function setting our game into motion :)
game_start()
        

