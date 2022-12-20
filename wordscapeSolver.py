def getLetters():
    letters = input("Type letters with a space in between each letter: ").split(' ')
    return letters

def checkLetter(word, letters):
    wordarray = []
    for letter in word:
        wordarray.append(letter)
    word = wordarray

    templetters = letters.copy()
    while (len(word) > 0):
        letterWord = word[0]
        if not (letterWord in templetters):
            return False
        else:
            templetters.remove(letterWord)
            word.pop(0)
    return True

def readDictionary(letters):
    dictionary = open("words.txt","r")
    words = []
    for word in dictionary:
        actualWord = word[:len(word)-1]
        if (len(actualWord) <= len(letters) and checkLetter(actualWord, letters)):
            words.append(actualWord)
    return words

def printWords(words):
    tempWords = words.copy()
    counter = 1
    while (len(tempWords) > 0):
        print(str(counter) + " letter words:")
        i = 0
        while( i < len(tempWords)):
            word = tempWords[i]
            if (len(word) == counter):
                print(word)
                tempWords.pop(i)
                i -= 1
            i += 1
        counter += 1
        
def printWords(words, num):
    tempWords = words.copy()
    i = 0
    while( i < len(tempWords)):
        word = tempWords[i]
        if (len(word) == num):
            print(word)
        i += 1

def checkSpecificWord(word, blank, indexArray):
    for i in indexArray:
        if not (word[i] == blank[i]):
            return False
    return True

def printSpecificWords(words, blank):
    indexArray = []
    for i in range(len(blank)):
        if not blank[i] == "_":
            indexArray.append(i)
    
    for word in words:
        if (len(word) == len(blank) and checkSpecificWord(word,blank,indexArray)):
            print(word)

    

def menuSystem(words):
    userInput = ""
    while (userInput != "q"):
        print("\nOptions:")
        print("\t1.) Print all words")
        print("\t2.) Print words with specified number of letters")
        print("\t3.) Print words that fit an unfinished word")
        userInput = input("What would you like? type the number of your choice or q to quit. ")
        if (userInput == "1"):
            printWords(words)
        elif (userInput == "2"):
            num = int(input("How many letters do you want in a word? "))
            printWords(words, num)
        elif (userInput == "3"):
            blank = input("Type the unfinished word using _ to specify a missing letter: ")
            printSpecificWords(words, blank)


if __name__=='__main__':
    menuSystem(readDictionary(getLetters()))
    

