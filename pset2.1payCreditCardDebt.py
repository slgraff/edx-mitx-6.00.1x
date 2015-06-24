# pset2.1payCreditCardDebt.py
# Problem Set 2, problem 1 - Paying Off Credit Card Debt

## Problem 1 - Paying the Minimum
## Write a program to calculate the credit card balance after one year
## if a person only pays the minimum monthly payment required by the
## credit card company each month.

# Data test cases
# Comment both of these out before submitting using online grader
# Test Case 1:
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Test Case 2:
# balance = 4842
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

totalPaid = 0.0
monthlyInerestRate = (annualInterestRate/12.0)



# Loop through twelve months, calculate interest, min payment, new balance
count = 1
while count <= 12:
    # Calculate the minimum monthly payment
    minMonthlyPayment = monthlyPaymentRate * balance

    # Update the balance to reflect payment
    balance -= minMonthlyPayment

    # Add monthly interest to balance
    balance += (monthlyInerestRate * balance)

    # Update the total amount paid
    totalPaid += minMonthlyPayment

    print "Month " + str(count)
    print "Minimum monthly payment: " + str(round(minMonthlyPayment, 2))
    print "Remaining balance: " + str(round(balance, 2))
    count += 1

print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))
