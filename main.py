import math

def main():

    txt = input("Welcome to the digital orthography corrector Pro 2.0!\n"
        "Do you have any doubts about the spelling of a word in English?\n"
        "Are you not sure if a word has a 'h‘ in it or not? Don’t worry! You came to the right place.\n"
        "With the digital orthography corrector Pro 2.0 you can insert a word in English and we will tell you if it appears in the Cambridge English dictionary.\n" 
        "If not, we are going to suggest you similar words, so that you can find the right one.\n"
        "IMPORTANT: Just one word at a time."
        "If you want to close the program, please type 'exit corrector'.\n"
        "Now type your word please and press enter: ")

    while txt != "exit corrector":
        txt = removeSpaceInfrontBehind(txt)
        while not onlyAlphabetCharacters(txt):
            txt = input("That's wrong. You can just use letters from the english alphabet.\n"
                  "You can't use spaces or any other symbol either!\n"
                  "Please insert a new word and press enter: ")
            txt = txt.replace(' ', '')

        txt = txt.upper()

        if search_word_in_file(txt):
            txt = input("This word is correct! But I'm still hungry. Gimme another word, please: ")
        else:
            recommend_words = find_recommended_word(txt)
            if len(recommend_words) == 0:
                print("This word doesn't exist!!!!!!")
            else:
                print("This word is a bit incorrect. Maybe your word is one in the list below: ")
                print(recommend_words)
            txt = input("Please insert a new word and press enter: ")

    print("Thanks for using our programm. Have a nice day!")

def onlyAlphabetCharacters(txt):
    for i in range(len(txt)):
        letter = ord(txt[i])
        if not (letter>64 and letter<91) and not (letter>96 and letter<123):
            return False
    return True

def removeSpaceInfrontBehind(txt):
    while txt[0] == ' ':
        txt = txt[1:]
    while txt[len(txt)-1] == ' ':
        txt = txt[:(len(txt)-1)]
    return txt


def search_word_in_file(word):
    file = open("generated_words.txt", "r")
    lines = file.readlines()
    num_lines = len(lines)

    top = num_lines
    bottom = 0
    pointer = math.floor((top + bottom) / 2)
    while word[0] != lines[pointer][0]:
        if word[0] > lines[pointer][0]:
            bottom = pointer
        if word[0] < lines[pointer][0]:
            top = pointer
        pointer = math.floor((top + bottom) / 2)

    direction = 1
    for index in range(1, len(word)-1):
        if word[index] > lines[pointer][index]:
            break
        if word[index] < lines[pointer][index]:
            direction = -1
            break

    while word[0] == lines[pointer][0]:
        if word + "\n" == lines[pointer]:
            return True
        else:
            pointer += direction

    return False


def find_recommended_word(input_word):
    file = open("generated_words.txt", "r")
    recommended_list = dict()

    for line in file:
        possibly_right_word = line.strip()

        check_grade = calculate_grade(input_word, possibly_right_word)

        if check_grade >= 75:
            recommended_list[possibly_right_word] = check_grade

    recommended_words = dict(sorted(recommended_list.items(), key=lambda x: x[1], reverse=True))

    return list(recommended_words)[:20]


def calculate_grade(input_word, possibly_right_word):
    check_grade = 100 - 8 * abs(len(input_word) - len(possibly_right_word))

    mark = 0
    unmatched_count = 0
    for index, letter in enumerate(possibly_right_word):
        if not mark < len(input_word):
            break
        if letter == input_word[mark]:
            mark += 1
            continue
        elif mark + 1 < len(input_word) and index + 1 < len(possibly_right_word) \
                and letter == input_word[mark + 1] and possibly_right_word[index + 1] == input_word[mark]:
            mark += 2
            index += 2
            check_grade -= 5
            continue
        else:
            is_found_in_the_rest = False
            for i in range(mark, len(input_word)):
                if input_word[i] == letter:
                    unmatched_count += (i - mark)
                    mark = i + 1
                    break
            if not is_found_in_the_rest:
                unmatched_count += 1

        check_grade -= unmatched_count * 5

    return check_grade


if __name__ == "__main__":
    main()
