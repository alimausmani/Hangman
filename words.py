
import random
import string

WORDLIST_FILENAME="words.txt"

def load_words():
    """
    Returns a list of valid words. words are string of lowercase letters.

    Depending on the size of the word list, this function may 
    take a while word to finish.
    """
    print("Loading word list from file...")
    # in file:file
    inFile=open(WORDLIST_FILENAME,'r')
    # line:string
    line=inFile.readline()
    # wordlist:list of string
    word_list=line.split()
    print(" ",len(word_list),"words loaded.\n\n")
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    return random.choice(word_list)
# Load the list of words into the variable word_list
# so that it can be accessed from anywhwere in the program
word_list=load_words()