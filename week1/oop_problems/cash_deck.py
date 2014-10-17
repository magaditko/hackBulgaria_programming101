import copy


class CashDesk:

    def __init__(self, money={100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money
        self.total_amount = 0

    def take_money(self, amount):
        for sum in amount:
            self.money[sum] += amount[sum]

    def total(self):
        for cash in self.money:
            self.total_amount += self.money[cash] * cash
        print(self.total_amount)

    def can_withdraw_money(self, amount):
        tmp = copy.deepcopy(self.money)
        if self.total_amount < amount:
            print(False)
        else:
            mm = [100, 50, 20, 10, 5, 2, 1]
            for cash in mm:
                while amount - cash >= 0:
                    if tmp[cash] > 0:
                        tmp[cash] -= 1
                    else:
                        print(False)
                    amount -= cash
            print(True)

my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
my_cash_desk.total()
my_cash_desk.can_withdraw_money(70)
