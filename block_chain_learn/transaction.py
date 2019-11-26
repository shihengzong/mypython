import datetime


class transaction:
    def __init__(self, payer, receiver, money, timestamp):
        self.payer = payer
        self.receiver = receiver
        self.money = money
        self.timestamp = timestamp

    def __repr__(self):  # __repr__ 对象描述类似于 tostring
        return str(self.payer) + "pay" + str(self.receiver) + str(
            self.money) + str(self.timestamp)
