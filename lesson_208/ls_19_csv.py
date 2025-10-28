# , 1,23 1.23 ;
import csv
from pathlib import Path

my_dir = Path(__file__).parent
just_file = my_dir / "just.csv"

with just_file.open(encoding="utf-8") as f:
    reader = csv.DictReader(f,)
    for row in reader:
        print(row, type(row))

data_list = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

just_out_file = my_dir / "just_out.csv"
with just_out_file.open("w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_STRINGS)
    writer.writerows(data_list)

# fieldnames = ['Name', 'Age', 'City']
# data_dict = [
#     {'Name': 'John', 'Age': 30, 'City': 'New York'},
#     {'Name': 'Alice', 'Age': 25, 'City': 'Los Angeles'},
#     {'Name': 'Bob', 'Age': 35, 'City': 'Chicago'}
# ]
# with just_out_file.open("w", newline='', encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";", quoting=csv.QUOTE_STRINGS)
#     writer.writerows(data_dict)
