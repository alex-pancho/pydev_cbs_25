class Money():

    def __init__(self, amount: float) -> None:
        self.__amount = amount
    
    @property
    def amount(self):
        return  self.__amount
    
    def __str__(self):
        return f"{self.__amount:.2f}"

    def __add__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            self.__amount += other.amount
        else:
            raise TypeError(f"Incorrect type for '{other}': {type(other)}")
    
    def __sub__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            self.__amount -= other.amount
        else:
            raise TypeError(f"Incorrect type for '{other}': {type(other)}")

    def __del__(self):
        pass
        # print("Del", self)


class UAH(Money):

    def __str__(self):
        return f"{self.amount:.2f} грн"


class USD(Money):

    def __str__(self):
        return f"${self.amount:.2f}"


class ForEx():

    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell
    
    def convert_to_usd(self, uah):
        if isinstance(uah, UAH):
            usd_amount = uah.amount / self.exchange_rate_sell
            return USD(usd_amount)
        else:
            raise TypeError(f"Incorrect type for '{uah}': {type(uah)}")

    def convert_to_uah(self, usd):
        if isinstance(usd, USD):
            uah_amount = usd.amount * self.exchange_rate_by
            return UAH(uah_amount)
        else:
            raise TypeError(f"Incorrect type for '{usd}': {type(usd)}")

if __name__ == "__main__":
    my_money = Money(100)
    # my_money.amount = 1000
    print(my_money, my_money.amount)
    sec_money = Money(10)
    my_money + sec_money
    print(my_money, my_money.amount)
    # my_money - 10
    # print(my_money)
    my_uah = UAH(5)
    my_usd = USD(75)
    small_usd = USD(5)
    # my_usd - my_uah
    my_usd - small_usd
    print(my_usd)
    my_1000_uah = UAH(1000)
    my_100_usd = USD(100)
    privatbank = ForEx(40.05, 41.50)
    accordbank = ForEx(41.05, 42.50)
    pb_to_uah = privatbank.convert_to_uah(my_100_usd)
    pb_to_usd = privatbank.convert_to_usd(my_1000_uah)
    acc_to_uah = accordbank.convert_to_uah(my_100_usd)
    acc_to_usd = accordbank.convert_to_usd(my_1000_uah)
    print(f"Продати Приват {my_100_usd}:", pb_to_uah)
    print(f"Купити Приват на {my_1000_uah}:", pb_to_usd)
    print(f"Продати  Ак{my_100_usd}:", acc_to_uah)
    print(f"Купити Ак на {my_1000_uah}:", acc_to_usd)



