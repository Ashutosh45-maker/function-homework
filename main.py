num=int(input("Enter any number for its factorial==>"))
factorial=1

if num<0:
    print("sorry,the factorial of neagative numbers does not exist")
elif num==0:
    print("the factorial of 0 is always 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)