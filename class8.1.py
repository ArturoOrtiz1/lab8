#This program determines how long it takes for an investment to double at a
#given interest rate
def main():
    invest=float(input("What is your investment value?"))
    annual=float(input("What is your current annualized interest rate written as 25%= 25?"))
    annual=annual/100
    years=0
    final=invest
    while final<=(invest*2):
      

        final= final+(final*annual)  
        years=years+1
    print("The number of years to double investment is,", years,"years")


    
main()
