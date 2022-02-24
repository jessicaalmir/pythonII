# Class BankAccount_175 to represent a bank account
class BankAccount_175:

    #Constructor definition
    def __init__(self, accountNumber_175, name_175, balance_175):
        # Class Attributes
        self.accountNumber_175 = accountNumber_175
        self.name_175 = name_175
        self.balance_175 = balance_175

    #Method deposit_175 to manage account deposits
    def deposit_175(self, newDeposit_175):
        self.balance_175 += newDeposit_175; #Increase balance
        print('Depost', newDeposit_175)

    #Method withdrawal_175 to manage account withdrawals
    def withdrawal_175(self,newWithdrawal):
        #Validate if withdrawal amount is more than the balance
        if(newWithdrawal > self.balance_175):
            print('Insuficient Balance')
        else:
            self.balance_175 -= newWithdrawal
            print('Withdrawal', newWithdrawal)

    #Method bankfees_175 to apply the banking fee with 4% of the account balance
    def bankfees_175(self):
        self.balance_175 -= (self.balance_175 * 0.04);
        print('Bank Fee charged:    4% ')

    #display_175 to display account details
    def display_175(self):
        print(f'Account Number: {self.accountNumber_175}')
        print(f'Account Name: {self.name_175}')
        print(f'Account Balance: {self.balance_175} $')
        print('-------------------------------')

#Program
account_175 = BankAccount_175('C0839175','Jessica Alvarez', 5000)
account_175.display_175()

#To make a withdrawal
account_175.withdrawal_175(500)
account_175.display_175()

#To make a deposit
account_175.deposit_175(80)
account_175.display_175()

#Bankfee charged
account_175.bankfees_175()
account_175.display_175()