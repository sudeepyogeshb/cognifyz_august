num=int(input("Enter a Number:"))
reverse=0
while num>0:
    r=num%10
    reverse=(reverse*10)+r
    num//=10
print("Reverse is:",reverse)