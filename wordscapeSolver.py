#Gets wordscape letters from user
def getLetters():
    letters = input("Type letters with a space in between each letter: ").split(' ')
    return letters

#Helper function that returns true
#if a word has some (if not) all letters
#in a wordscape
def checkLetter(word, letters):
    #turn word into word array
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

#reads dictionary and places applicable words
#in an array
def readDictionary(letters):
    dictionary = open("words.txt","r")
    words = []
    for word in dictionary:
        actualWord = word[:len(word)-1]
        if (len(actualWord) <= len(letters) and checkLetter(actualWord, letters)):
            words.append(actualWord)
    return words

#prints all words
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

#prints all words with a specified
#amount of letters        
def printWords(words, num):
    tempWords = words.copy()
    i = 0
    while( i < len(tempWords)):
        word = tempWords[i]
        if (len(word) == num):
            print(word)
        i += 1

#helper function that see if a specific word
#fits the requirement of the incomplete word
def checkSpecificWord(word, blank, indexArray):
    for i in indexArray:
        if not (word[i] == blank[i]):
            return False
    return True

#Returns all words that satisfy 
#the incomplete word
def printSpecificWords(words, blank):
    indexArray = []
    for i in range(len(blank)):
        if not blank[i] == "_":
            indexArray.append(i)
    
    for word in words:
        if (len(word) == len(blank) and checkSpecificWord(word,blank,indexArray)):
            print(word)

    
#menu system that allows user to choose what they want
def menuSystem(words):
    userInput = ""
    while (userInput != "q"):
        print("\nOptions:")
        print('\t0.) Choose new letters')
        print("\t1.) Print all words")
        print("\t2.) Print words with specified number of letters")
        print("\t3.) Print words that fit an unfinished word")
        userInput = input("What would you like? Type the number of your choice or q to quit. ")
        if (userInput == "0"):
            menuSystem(readDictionary(getLetters()))
            break;
        elif (userInput == "1"):
            printWords(words)
        elif (userInput == "2"):
            num = int(input("How many letters do you want in a word? "))
            printWords(words, num)
        elif (userInput == "3"):
            blank = input("Type the unfinished word using _ to specify a missing letter: ")
            printSpecificWords(words, blank)


if __name__=='__main__':
    menuSystem(readDictionary(getLetters()))
    

