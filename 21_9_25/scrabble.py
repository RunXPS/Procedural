from sys import argv

def d_and_c(word, filename):
    word = (word.upper())
    found = False
    with open(filename, "r") as fp:
        wordlist = fp.readlines()
        for i in range(len(wordlist)):
            wordlist[i] = wordlist[i].strip("\n")
            wordlist[i] = wordlist[i].strip(" ")
        while (found == True) is False:
            if len(wordlist) == 1 and wordlist[len(wordlist)//2] != word:
                break
            if wordlist[len(wordlist)//2] > word:
                wordlist = wordlist[:len(wordlist)//2]
            elif wordlist[len(wordlist)//2] < word:
                wordlist = wordlist[len(wordlist)//2:]
            else:
                if wordlist[len(wordlist)//2] == word:
                    found = True
                    break
                break
        return found
def main ():
    input_file = "scrabble.txt"
    word = argv[1]
    print(d_and_c(word,input_file))
main()