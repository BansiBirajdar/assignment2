'''Write a program which accept one number and display below pattern.
Input : 5
Output : 
* * * * *
* * * *
* * *
* *
*'''
def Display(no):
    if(no<=0):
        print("please enter the positive number")
        return 
    for i in range(1,no+1):
        for j in range(1,no+1):
            if(j>=i):
                print("*",end="\t")
        print("\n")
def main():
    no=int(input("enter the number="))
    Display(no)
if (__name__=="__main__"):
    main()