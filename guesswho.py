import random

class Character:
    """ This class holds a character's name and it's traits """

    def __init__(self, name, backpack, glasses, hat, piercing):
        self.name = name
        self.backpack = backpack
        self.glasses = glasses
        self.hat = hat
        self.piercing = piercing
    
    def __str__(self):
        ''' return a string with the name and attributes'''

        # finish writing this method to return the name and the values for each of the 
        # boolean attributes (backpack, glasses, hat, piercing)
        pass
    
    def get_match_result(self, type, guess):

        ''' Get the result of the type of guess and guess.  Return True or False'''
        if type == "b":
            if guess == "T" and self.backpack:
                return True
            elif guess == "F" and not self.backpack:
                return True
            else: 
                return False

        elif type == "g":
            if guess == "T" and self.glasses:
                return True
            elif guess == "F" and not self.glasses:
                return True
            else:
                return False

        elif type == "h":
            if guess == "T" and self.hat:
                return True
            elif guess == "F" and not self.hat:
                return True
            else:
                return False

        elif type == "p":
            if guess == "T" and self.piercing:
                return True
            elif guess == "F" and not self.piercing:
                return True
            else:
                return False
        return False

class GuessWho:
    ''' repressents the guess who game '''
    
    def __init__(self):
        ''' inititalize the game '''

        # finish setting up the list of characters for the game
        # each should have a unique combination of the 4 attributes (TTTT, TTTF, TTFF, FFFF, etc)
        ch1 = Character()
        ch2 = Character()
        ch3 = Character()
        ch4 = Character()
        ch5 = Character()
        ch6 = Character()
        ch7 = Character()
        ch8 = Character()

        self.char_list = [ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8]

        # finish picking a character at random
        self.picked = 

        # set done to false

        # initialize the number of correct guesses to 0
        

    def play(self):
        ''' play the game '''

        # print all the characters in the game

        # while the game isn't done

            # get the current attribute (b, g, h, or p) and guess (T or F)
            curr_type = input("What attribute do you want to guess on?  Enter b (backpack), g (glasses), h (hat), or p (piercing): ")
            curr_guess = input("For that attribute guess T for True or F for False: ")

            # get the result of the guess (either True or False)
            result = self.picked.get_match_result(curr_type,curr_guess)

            # if the result was True tell the player that the guess was correct

                # increment the number of correct guesses

                # if the number of correct guesses is 4 then the player won
                # tell the player and set done to true

            # otherwise tell the player the guess was not correct for that attribute

def main():
    game = GuessWho()
    game.play()

if __name__ == "__main__":
    main()
    




       