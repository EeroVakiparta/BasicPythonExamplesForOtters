import random

# dictionary which contains english words and their finnish translations
easy_words = {
    "cat": "kissa",
    "dog": "koira",
    "house": "talo",
    "car": "auto",
    "table": "pöytä",
    "chair": "tuoli",
    "window": "ikkuna",
    "door": "ovi",
    "pen": "kynä",
    "pencil": "kynä",
    "book": "kirja",
    "bottle": "pullo",
    "glass": "lasi",
    "cup": "kuppi",
    "plate": "lautanen",
    "fork": "haarukka",
}

medium_words = {
    "computer": "tietokone",
    "mouse": "hiiri",
    "keyboard": "näppäimistö",
    "monitor": "näyttö",
    "printer": "tulostin",
    "laptop": "kannettava tietokone",
    "phone": "puhelin",
    "camera": "kamera",
    "television": "televisio",
}

hard_words = {
    "chairman": "puheenjohtaja",
    "rakkaus": "love",
    "sorry": "anteeksi",
    "thank you": "kiitos",
    "excuse me, do you know a way to the train station?": "antaa anteeki, tiedätkö tien junaasemalle?"
}




# function which takes parameter word and gives back the translation
def translate(word):
    if word in easy_words:
        return easy_words[word]
    elif word in medium_words:
        return medium_words[word]
    elif word in hard_words:
        return hard_words[word]
    else:
        return "Word not found"

# function which takes difficulty as parameter and gives back a random word from that difficulty
def random_word(difficulty):
    if difficulty == "easy":
        return random.choice(list(easy_words.keys()))
    elif difficulty == "medium":
        return random.choice(list(medium_words.keys()))
    elif difficulty == "hard":
        return random.choice(list(hard_words.keys()))
    else:
        return "Difficulty not found"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # take user input and name it difficulty
    score = 0
    difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")

    # check if difficulty is valid if not ask again
    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        print("Sorry " + difficulty + " is not a valid difficulty. Please try again.")
        difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ")


    # call the function random_word and give it the parameter difficulty
    word = random_word(difficulty)

    #keep asking for the translation until the user gives the correct answer if answer is correct print "Correct!" and increment the score by 1. Ask total of 10 words
    for i in range(10):
        print("Translate " + word)
        answer = input()
        if answer == translate(word):
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is " + translate(word))
        word = random_word(difficulty)

    # print the score and the percentage of correct answers and thank the user for playing
    print("Your score is " + str(score) + "/10")
    print("You got " + str(score * 10) + "% correct")
    print("Thank you for playing Eeros language learner!")