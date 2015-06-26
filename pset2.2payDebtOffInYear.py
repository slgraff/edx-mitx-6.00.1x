# pset2.2payDebtOffInYear.py
# Problem Set 2, Problem 2 - Paying Debt Off in a Year

# Now write a program that calculates the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does
# not change each month, but instead is a constant amount that will
# be paid each month.

# Interest is calculated each month after payment is deducted
# Monthly payment must be a multiple of $10

# Test cases, comment out before submitting for grading
# Test Case 1:
balance = 3329
annualInterestRate = 0.2

# Test Case 2:
# balance = 4773
# annualInterestRate = 0.2
#
# Test Case 3:
# balance = 3926
# annualInterestRate = 0.2

# Copy balance into myBalance
# myBalance = balance

# Loop through to determine minimum fixed payment to pay off in one Year
# Start with $10 payments, increase by $10 each iteration

# Initialize minimum monthly fixed payment
minimumFixedPayment = 0.0

# Copy balance into myBalance
myBalance = balance

# Monthly interest rate
monthlyInterestRate = annualInterestRate/12.0

# Loop through calculating if monthly payment will pay off in 12 months
while myBalance > 0.0:

    # Increment minimum monthly fixed payment by $10 each time through loop
    minimumFixedPayment += 10.0

    # Apply payments and interest for each of twelve months
    # Once balance at end is less then 0 will have
    # calculated min fixed payment
    for month in range (0, 12):

        # Apply payment to balance
        myBalance -= minimumFixedPayment

        # Add interest to balance
        myBalance += (myBalance * monthlyInterestRate)

    if myBalance > 0:
        # Reset balance each time through loop
        myBalance = balance


    # Debugging print statement
    # print "Exited for loop"
    # print "Min payment " + str(round(minimumFixedPayment, 0))


# Print the lowest monthly payment that will pay off the debt in 12 months
print "Lowest Payment " + str(minimumFixedPayment)
