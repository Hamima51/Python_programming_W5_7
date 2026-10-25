DELIMITER = ","


def collectWords():
    words = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if words == "":
            words = word
        else:
            words = words + DELIMITER + word
    return words


def analyseWords(words):
    if words == "":
        wordList = []
    else:
        wordList = words.split(DELIMITER)

    wordCount = len(wordList)
    charCount = sum(len(word) for word in wordList)
    average = charCount / wordCount if wordCount > 0 else 0.0

    print(f"- {wordCount} Words")
    print(f"- {charCount} Characters")
    print(f"- {average:.2f} Average word length")


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")


main()