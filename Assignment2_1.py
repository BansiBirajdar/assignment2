'''Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.'''
import Arithmetic

def main():
    no1=int(input("enter the no1="))
    no2=int(input("enter the no2="))
    ans=Arithmetic.Add(no1,no2)
    print("\n    Addition is=",ans)
    ans=Arithmetic.Sub(no1,no2)
    print("\nSubstraction is=",ans)
    ans=Arithmetic.Mult(no1,no2)
    print("\nMultiplicaton is= ",ans)
    ans=Arithmetic.Div(no1,no2)
    print("\n     Division is=",ans)

if(__name__=="__main__"):
    main()
    