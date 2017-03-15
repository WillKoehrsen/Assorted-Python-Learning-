#written by usingpython.com

#allows us to access a random 'key' in the dictionary
import random

#the questions/answer dictionary
my_dict =   {
                "Base-2 number system" : "binary",
                "Number system that uses the characters 0-F" : "hexidecimal",
                "7-bit text encoding standard" : "ascii",
                "16-bit text encoding standard" : "unicode",
                "A number that is bigger than the maximum number that can be stored" : "overflow",
                "8 bits" : "byte",
                "1024 bytes" : "kilobyte",
                "Picture Element. The smallest component of a bitmapped image" : "pixel",
                "A continuously changing wave, such as natural sound" : "analogue",
                "the number of times per second that a wave is measured" : "sample rate",
                "A bunary representation of a program" : "machine code"
            }

#welcome message
print("Computing Revision Quiz")
print("=======================")

#the quiz will end when this variable becomes 'False'
playing = True

#While the game is running
while playing == True:

    #set the score to 0
    score = 0

    #gets the number of questions the player wants to answer
    num = int(input("\nHow many questions would you like: "))

    #loop the correct number of times
    for i in range(num):

        #the question is one of the dictionary keys, picked at random
        question = (random.choice( list(my_dict.keys())))
        #the answer is the string mapped to the question key
        answer = my_dict[question]

        #print the question, along with the question number
        print("\nQuestion " + str(i+1) )
        print(question  + "?")

        #get the user's answer attempt
        guess = input("> ")

        #if their guess is the same as the answer
        if guess.lower() == answer.lower():
            #add 1 to the score and print a message
            print("Correct!")
            score += 1
        else:
            print("Nope!")

    #after the quiz, print their final score  
    print("\nYour final score was " + str(score))

    #store the user's input...
    again = input("Enter any key to play again, or 'q' to quit.")

    #... and quit if they types 'q'
    if again.lower() == 'q':
        playing = False
