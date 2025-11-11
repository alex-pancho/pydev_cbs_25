import csv
from pathlib import Path


file_path = Path(__file__).parent / "users_1.csv"

with file_path.open(encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    persons_list = [person for person in reader]

for row in persons_list:
    print(row)

with file_path.open(encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    out = list(reader)

print(out)

newfile_path = Path(__file__).parent / "users_2.csv"
with newfile_path.open("w", encoding="utf8", newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=';')
    writer.writerows(out)

