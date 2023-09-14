import re 

#function to validate email
def validtest(email):

    #creating a email format
    email_format=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    #comparing user email with the format
    if(re.match(email_format,email)):
        print("valid email")
    else:
        print("invalid email")  


#user email input
email=input("enter a email: ")

#calling validate function
validtest(email)