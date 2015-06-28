# pset2.3-bisectionSearch.py
# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Problem Set 2, problem 3

# Use bisection search to make the program faster

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Problem Summary: Use bisection search to search for the smallest monthly payment
# to the cent such that we can pay off the entire balance within a year.

# Test Cases, comment out before submitting for grading
# Test Case 1
##balance = 320000
##annualInterestRate = 0.2

##Test Case 2
##balance = 999999
##annualInterestRate = 0.18

# Calculate monthly interest rate, lower and upper payments
monIntRate = (annualInterestRate / 12.0)
paymentLower = (balance / 12)
paymentUpper = (balance * ((1 + monIntRate)**12)) / 12.0

# Keep a copy of the balance in origBalance
origBalance = balance

while balance != 0.00:
    # Set value for thePayment to midpoint of lower and upper
    thePayment = (paymentLower + paymentUpper) / 2

    # Reset balance each time through while loop
    balance = origBalance

    for i in range(1,13):
        balance = ((balance - thePayment) * (1 + monIntRate))

    if balance > 0:
        paymentLower = thePayment

    elif balance < 0:  
        paymentUpper = thePayment

    balance = round(balance, 2)

print "Lowest Payment: " + str(round(thePayment,2))
