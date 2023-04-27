def onlyAlphabetCharacters(txt):
    for i in range(len(txt)):
        letter = ord(txt[i])
        if not (letter>64 and letter<91) and not (letter>96 and letter<123):
            return False
    return True

def main():

    txt = input("Welcome to the digital orthography corrector Pro 2.0!\n"
        "Do you have any doubts about the spelling of a word in English?\n"
        "Are you not sure if a word has a 'h‘ in it or not? Don’t worry! You came to the right place.\n"
        "With the digital orthography corrector Pro 2.0 you can insert a word in English and we will tell you if it appears in the Cambridge English dictionary.\n" 
        "If not, we are going to suggest you similar words, so that you can find the right one.\n"
        "IMPORTANT: Just one word at a time."
        "If you want to close the program, please type 'exit corrector'.\n"
        "Now type your word please and press enter: ")

    while(txt != "exit corrector"):
        txt = txt.replace(' ', '')
        while(not onlyAlphabetCharacters(txt)):
            txt = input("That's wrong. You can just use letters from the english alphabet.\n"
                  "Please insert a new word and press enter: ")
            txt = txt.replace(' ', '')
        txt = txt.upper()

        # PHUC PART

        txt = input("Please insert a new word and press enter: ")

    print("Thanks for using our programm. Have a nice day!")

if __name__ == "__main__":
    main()