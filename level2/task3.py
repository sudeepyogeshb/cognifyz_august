import re

check_pass = re.compile(r'''(
^.*(?=.{10,})           # Checking the length, minimum 8
(?=.*\d)                # Numeric Digits
(?=.*[a-z])             # Lowercase, a to z.
(?=.*[A-Z])             # Uppercase, A to Z
(?=.*[@#$%^&+=!]).*$    # Special Characters
)''',re.VERBOSE)

passCode = input('Enter the Password: ')
mo1 = check_pass.search(passCode)

# Check the password is validate or not
if mo1:
    print("Strong Password.")
else:
    print("Weak Password.")