# JavaScript Object Notation - JSON
import json
from pathlib import Path

my_dir = Path(__file__).parent
load_file = my_dir / "_login.json"

try:
    with load_file.open(encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            print("Read data error, try again later")
            data = None
except FileNotFoundError:
    data = None
    print("Файл не знайдено")

print(data, type(data))

json_string = '{"name": "John", "age": 30, "city": "New York"}'
str_data = json.loads(json_string)
print(str_data)

data_to_json = {
    "name": "Oleksandra",
    "learn_year": 2025,
    "is_finished": False,
    "link_to_cert": None,
    "name2": {"name": "Oleksandra",
    "learn_year2": 2025,
    "is_finished2": False,
    "link_to_cert2": None,}
}

def save_to_json(data_to_json:dict, file_name:str = "out.json"):
    output_file = my_dir / file_name
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data_to_json, f, indent=2)

save_to_json(data_to_json, "out.json")

my_swagger = my_dir / "swagger.json"
with my_swagger.open(encoding="utf-8") as f:
    data_sw = json.load(f)

save_to_json(data_sw, "swagger_pp.json")
