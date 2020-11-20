 LoanAmount = int(input('The Loan Amount Is :'))
 AnnualInterestRate  = int(input('The Annual Interest Rate Is :'))
 MonthlyPayment = int(input('The Monthly Payment Is :'))

 StartingBalance = LoanAmount
 Payment = MonthlyPayment
 MiddleBalance = StartingBalance - Payment 
 Interest =  MiddleBalance * AnnualInterestRate/12/100
 EndingBalance = MiddleBalance + Interest

 >>> print('''
	Starting            Middle              Ending
Month	Balance   Payment   Balance   Interest  Balance
-------------------------------------------------------
''')
 for i in range(1,5):
	print('%8d%10.2f10.2f10.2f10.2f10.2f'%(i,
                                               StartingBalance,
                                               Payment,
                                               MiddleBalance,
                                               Interest,
                                               EndingBalance)
