from Recap.until1 import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__("Giri", 1000000000, 10019)

    def final(self):
        print(f'Public (account_holder): {self.account_holder}')      # ✅ Accessible
        print(f'Protected (_balance): {self._balance}')               # ✅ Accessible by convention
        # print(self.__pin)  ❌ will raise AttributeError
        print(f'Private (__pin) via getter: {self.BankAccount.__pin}')        # ✅ Proper way
                           # ✅ Accessible
obj=SavingsAccount()
obj.final()
