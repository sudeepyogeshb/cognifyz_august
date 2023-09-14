#checks if the given string is planidrome
def ispalindrome(string):

    #compares string and its reversed srting
    if(string==string[::-1]):
        print("string is a palindrome")
    else:
        print("string is not a plaindrome")

#input of string
string=input("enter a word: ")

#calling the ispalindrome function
ispalindrome(string)