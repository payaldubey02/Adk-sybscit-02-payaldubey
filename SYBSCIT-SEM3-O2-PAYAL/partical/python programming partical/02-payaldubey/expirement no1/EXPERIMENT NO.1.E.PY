# PYTHON PROGRAMM TO CHECK IF THE NUMBER IS PROVIDED BY THE USER IS AN ARMSTRONG NUMBER OR NOT
def armstrong(num):
    sum=0
    # find the sum of the cube of each digit
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    # display the result
    if num==sum:
        print(num,"is an armstrong number")
    else:
        print("is not an armstrong number")

def palindrome(num):
    n=num
    rev=0
    while num !=0:
        rev=rev *10
        rev=rev +int(num%10)
        num=int(num/10)
    if n== rev:
        print(n,"is pelindrome number")
    else:
        print(n,"is not palin")

# take input from the user
num=int(input("enter a number to check it is armstrong or not:"))
armstrong(num)
# take input from the user
num=int(input("enter a number to check it is palidrome or not:"))
palidrome(num)

        
    
