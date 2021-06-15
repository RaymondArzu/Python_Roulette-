import random
n = 0
colorOption = "none"
startingDeposit = 0
moneyBalance = 1000.00
guessNumber = 0

Bid=0

def numberBeingBetOn():

    numberGuess = input("Please enter the number you are betting on (0 - 49) : ")
    convertNumber = int(numberGuess)
    if convertNumber > 49 or convertNumber < 0:
        print("The number you selected is outside the indcated range (0 - 49)\n Please select a number between 0 and 49 \n\n")
    else:
        getColor = getNumberColor(convertNumber)
        print("The number you are betting on is: ", getColor,numberGuess, "\n\n")
    
        getNumberColor(convertNumber)
        placeBid(convertNumber)


def placeBid(numberGuess):
    global moneyBalance
   
    Bid = input("Place the amount of money you will be betting: $")
    convertBid = float(Bid)
    if moneyBalance > convertBid:

        print("You placed a bid of: $",Bid)  
        convertBid= float(Bid)
        updateMoneyBalance(moneyBalance,convertBid)
        
        
        generatedNumber = random.randint(0,49)
        verifyWinner(numberGuess,generatedNumber,Bid)
    else: 
        breaklines = "\n\n"
        print("Your bid exceeds your current balance of $", moneyBalance, breaklines)

def mergeNumberWithColor(selection, color, guessNumber):
    print(selection, color, guessNumber)

def getNumberColor(guessNumber):
    global colorOption
    
    #guessNumber= input("Select a Number: ")
    if guessNumber % 2 == 0:
        colorOption = "black" 
    else:
        colorOption ="red"
    
    return colorOption
   # youSelect = "You selected "
   # mergeNumberWithColor(youSelect,guessNumber, colorOption)


def updateMoneyBalance(presentBalance, moneyPlacedOnBet):
    global moneyBalance
    moneyBalance = presentBalance - moneyPlacedOnBet

    stringMoneyBalance = str(moneyBalance)
    print("Your present balance is: $", moneyBalance)

  

def verifyWinner(guessNumber,randomNumber,theBid):
    if guessNumber == randomNumber:
        print("We have a winner here" ) 
        calculateWinnings(theBid)
    else:
        print("Sorry try again") 
        convertNumber = int(randomNumber)
        getColor = getNumberColor(convertNumber)
        backBracket = ")"
        print("The ball landed on: (",getColor ,randomNumber, backBracket)      

def calculateWinnings(moneyPlacedOnBet):
    winnings = moneyPlacedOnBet * 50
    print("You have won the lumpSum of: $")

        #makeDeposit()

#def makeDeposit():
#    startingDeposit = input("Enter Starting Deposit:")
#   moneyBalance =+ startingDeposit        
    
while moneyBalance > 0:
    numberBeingBetOn()

    
    #if moneyBalance < 10:
    #    makeDeposit()
   # else:    
    
print("thank You for playing")