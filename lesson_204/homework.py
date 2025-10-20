"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    result = []
    
    if not isinstance(string_list, list):
        raise ValueError("Input i not a list!")
    elif len(string_list):
        for item in string_list:
            try:
                if isinstance(item, str):
                    lst = list(item.split(","))

                    tot_sum = 0
                    for i in lst:
                        tot_sum += (int)(i)
                    result.append(tot_sum)
                else:
                    raise AttributeError("Не можу це зробити! AttributeError")
            except ValueError as e:
                result.append("Не можу це зробити!")
            except AttributeError as e:
                result.append(e.args[0])
    else:
        raise ValueError("Empty input list! ValueError") 
    
    return result


if __name__ == "__main__":

    sum_numbers_in_list([])
    sum_numbers_in_list("21")
    

    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])
    print(output)

    output = sum_numbers_in_list(
                [
                    "1,2,3,4",
                    "1,2,3,4,50",
                    "qwerty1,2,3",
                    {"country": "Ukraine", "continent": "Europe", "size": 123},
                ]
            )
    #[10,  60, "Не можу це зробити!", "Не можу це зробити! AttributeError", ]
    print(output)
    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """
