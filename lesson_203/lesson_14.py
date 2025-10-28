class Money():

    def __init__(self, amount: float) -> None:
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount

    def __str__(self):
        return f"{self.__amount:.2f}"
    
    def __add__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.__amount + other.get_amount())
        elif isinstance(other, (int, float)):
            return type(self)(self.__amount + other)
        else:
            raise ValueError(f"Incorrect type for '{other}'")
    
    def __sub__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.__amount - other.get_amount())
        elif isinstance(other, (int, float)):
            return type(self)(self.__amount - other)
        else:
            raise ValueError(f"Incorrect type for '{other}'")


class UAH(Money):

    def __str__(self):
        return f"{self.get_amount():.2f} грн"


class USD(Money):

    def __str__(self):
        return f"${self.get_amount():.2f}"


class ForEx():

    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell
    
    def convert_to_usd(self, uah_amount):
        if isinstance(uah_amount, UAH):
            usd_amount = uah_amount.get_amount() / self.exchange_rate_sell
            return USD(usd_amount)
        else:
            raise ValueError(f"Incorrect type for '{uah_amount}'")
    
    def convert_to_uah(self, usd_amount):
        if isinstance(usd_amount, USD):
            usd_amount = usd_amount.get_amount() * self.exchange_rate_by
            return UAH(usd_amount)
        else:
            raise ValueError(f"Incorrect type for '{usd_amount}'")


if __name__ == "__main__":
    my_money = Money(100)
    print(my_money)
    my_wife_money = Money(10000)
    toltal_money = my_money + my_wife_money
    print(toltal_money, type(toltal_money))
    my_money_new = my_money + 25
    print(my_money_new)
    my_money_new = my_money_new - 120
    print(my_money_new)
    my_uah = UAH(5)
    print(my_uah)
    my_uah_2 = UAH(95)
    print(my_uah_2)
    all_money = my_uah + my_uah_2
    print("UAH money", all_money)
    my_usd = USD(75)
    my_new_usd = my_usd + USD(25)
    print("usd money", my_new_usd)
    privatbank = ForEx(42.05, 43.57)
    pb_to_uah = privatbank.convert_to_uah(my_new_usd)
    pb_to_usd = privatbank.convert_to_usd(all_money)
    print(f"Продати {my_new_usd}:", pb_to_uah)
    print(f"Купити на {all_money}:", pb_to_usd)
