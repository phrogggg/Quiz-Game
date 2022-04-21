from PIL import Image
import time
import random
def wrong_answer():
    print("Enter a valid input.")


def quiz():
    score = 0
    while True:
        q_1 = input("Question 1: Can a grizzly bear beat a silverback gorilla in a fight (T) or (F): ").upper()
        if q_1 == "T":
            print("Great job, your answer is correct!")
            score = score + 1
            print(f"Your current score is {score}")
        elif q_1 == "F":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")

        
        q_2 = input(f"Can fleas jump 250 times their body length (T) or (F): ").upper()          
        if q_2 == "T":
            print("Good job, your answer was correct!")
            score = score + 1
            print(f"Your current score is {score}")
        elif q_2 == "F":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")            
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")

        q_3 = input("Are humming birds the only birds that can fly backwards (T) or (F): ").upper()
        if q_3 == "T":
            print("Great job, you got the answer correct!")
            score = score + 1
            print(f"Your current score is {score}")
        elif q_3 == "F":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        
        image1 = Image.open("Capybara.jpg")
        image1.show()
        q_4 = input("Is this a Capybara (Y) or (N): ").upper()
        if q_4 == "Y":
            print("Great job, you answer was correct!")
            score = score + 1
            print(f"Your score is now {score}")
        elif q_4 == "N":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass 
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        
        image2=Image.open("orbweaver.jpg")
        image2.show()
        q_5 = input("Can this spider kill you (Y) or (N): ").upper()
        if q_5 == "N":
            print("Great job, your answer was correct!")
            score = score + 1
            print(f"Your score is now {score}")
        elif q_5 == "Y":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")

        q_6 = input("Only female mosquitos bite (T) or (F): ").upper()
        if q_6 == "T":
            print("Great job, you got the answer")
            score = score + 1
            print(f"Your score is now {score}")
        elif q_6 == "F":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")

        q_7 = input("Mantis shrimp has the worlds fastest punch (T) or (F): ").upper()
        if q_7 == "T":
            print("Great job, your answer was correct!")
            score = score + 1 
            print(f"Your score is now {score}")
        elif q_7 == "F":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        
        q_8 = input("Male lions do most of the hunting (T) or (F): ").upper()
        if q_8 == "F":
            print("Great job, your answer was correct!")
            score = score + 1
            print(f"Your score is now {score}")
        elif q_8 == "T":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        
        q_9 = input("There are some pigs that are as big as bears (T) or (F): ").upper()
        if q_9 == "T":
            print("Great job, your answer was correct!")
            score = score + 1
            print(f"Your score is now {score}")
        elif q_9 == "F":
            print("Too bad, your answer was incorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")

        q_10 = input("The executioner wasp has the most painful sting in the world (T) or (F): ").upper()
        if q_10 == "F":
            print("Great job, your answer was correct!")
            score = score + 1
            print(f"Your score is now {score}")
        elif q_10 == "T":
            print("Too bad, your answer was inocorrect!")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your score is now {score}")
        else:
            print("Thats not a valid response, you lose a point.")
            if score == 0:
                pass
            elif score > 0:
                score = score - 1
            print(f"Your current score is {score}")
        
        percent = score/10 * 100
        print(f"You got {percent}% Total!")

        replay = input("Do you want to play again (Y) or quit (Q): ").upper()
        if replay == "Y":
            quiz()
        elif replay == "Q":
            print("Exiting in 5 seconds.")
            time.sleep(5)
            exit()
        else:
            print("Please enter a valid input.")
            



while True:
    startup = input("Do you want to play a quiz (Y) or (N): ").upper()
    if startup == ("Y"):
        quiz()
    elif startup == ("N"):
        print("Exiting in 5 seconds.")
        time.sleep(5)
        exit()
    else:
        print("Please enter a valid response.")