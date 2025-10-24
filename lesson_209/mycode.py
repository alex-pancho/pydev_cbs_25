import sys
from pathlib import Path
project_dir = Path(__file__).parent.parent
sys.path.append(str(project_dir))
print(sys.path)
from lesson_208.ls_19_json import save_to_json, data_to_json

def sum_len_string(*args):
    total = 0
    for a in args:
        if isinstance(a, str):
            total += len(a)
    return total

def func_a():
    pass

def func_b():
    pass

def func_c():
    pass

def func_d():
    pass

def func_e():
    pass

if __name__ =="__main__":

    save_to_json(data_to_json)
    tot = sum_len_string("a", "bb", "cc")
    print("sum_len_string", tot)