# Denis Glazer, CS110A  
# Homework 7 -- Palindrome detector 
#This program designed to examine a user-entered string to determine if it's a palindrome.

def palindrom(allTogether):
  '''
  This function makes make my program to check for palindromic words or phrases: removes all punctuation and spacing, then checks if it's a palindrome
  '''
  myPhrase = [c for c in allTogether.lower() if c.isalpha()]
  return (myPhrase == myPhrase[::-1])


def inputProccess():
  '''
  This function recieves users input, pass it to palindrom() function, receives answer and notifies user if input was a palidrom or not 
  '''
  userInput = input("Please enter a word or phrase: ")
  if palindrom(userInput):
    print ("The text you entered: '%s' is a palindrome" % userInput)
  else:
    print ("The text you entered: '%s' is not a palindrome" % userInput)


def main():
  '''
  This function asks the user if they want to enter another word or phrase, and if the user types "yes" or "y", upper or lower case, then the program should repeat.
  '''
  inputProccess()
  print("\n")
  newGame = input("Do you want to enter another word? ").lower()
  while newGame == "yes" or newGame == "y":
    inputProccess()
    print("\n")
    newGame = input("Do you want to enter another word? ").lower()
  print("Bye bye, see you next time")

main()
