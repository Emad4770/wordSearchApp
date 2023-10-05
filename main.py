
def main():
    userInput = input('Enter name of the files please: ')
    fileNamesList = userInput.split(",")
    keyWord = input('Enter the word to search for:  ')

    for fileName in fileNamesList:
        inFile = open(fileName, 'r')
        for line in inFile:
            if keyWord.casefold() in line.casefold():
                print(f'{fileName}: {line}')
        inFile.close()

if __name__ == '__main__':
    main()

