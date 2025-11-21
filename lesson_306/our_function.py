def is_data_list_type(arr):
    return isinstance(arr, (list, tuple))


def sum_list_last_first(arr: list | tuple) -> float:
    result = None
    if not is_data_list_type(arr):
        raise ValueError("List or tuple variable type expected")
    # add check is arr[0] + arr[-1] != 0
    if len(arr) >= 2:
        if arr[0] + arr[-1] == 0:
            raise ZeroDivisionError(f"Get val1: {arr[0]} and val2: {arr[-1]}," \
                              "sum expected non-zero")
        result = sum(arr) / (arr[0] + arr[-1])
    return result


if __name__ == "__main__":
    my_list = [1, 3, 7]
    out = sum_list_last_first(my_list)
    print("We get here: ", out)
