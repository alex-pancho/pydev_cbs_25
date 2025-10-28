from mycode import (
    sum_len_string, 
    func_a, 
    func_e
)

from calc import func_a as calc_a, func_b as calc_b
from calc import some_extra_long_and_wery_long_named_function as SELN


if __name__ =="__main__":
    tot = sum_len_string("aaa", "s", "pep8")
    print("sum_len_string", tot)
    func_a()
    func_e()
    calc_a()
    calc_b()
    SELN()