from pathlib import Path

# file = open("test.txt", "r", encoding="utf8")
# print(file)
# print(file.readlines())
# file.close()
try:
    with open("test.txt", "r", encoding="utf8") as f:
        text = f.readlines()
        print(text)
except FileNotFoundError as e:
    pass ##

# for_file = """
# with open("test.txt", 'w', encoding='utf-8') as f:
#     f.write("my first file\\n")
#     f.write("This file\\n\\n")
#     f.write("contains three lines\\n")
# """
# with open("test.py", "w", encoding="utf8") as f:
#     f.writelines(for_file)

# with open("test.txt", 'r', encoding='utf-8') as f:
#     print(f.read(7))
#     print(f.read(15))
#     print(f.read(10))

my_line = "abcd e\n"
with open("test_2.txt", "a", encoding="utf8") as f:
    f.writelines(my_line)

print(__file__, type(__file__))
my_file_path = Path(__file__)
print(my_file_path, type(my_file_path))
project_path = my_file_path.parent.parent
print(project_path)
print(project_path.is_dir())
test_3_path = project_path / "test_3.txt"
print(test_3_path)
print(test_3_path.is_dir())
print(test_3_path.is_file())
print(test_3_path.exists())
print(test_3_path.chmod(777))

with test_3_path.open("r", encoding="utf8") as f:
        text = f.readlines()
        print(text)

dirs = [d for d in project_path.iterdir() if d.is_dir()]
print(dirs)
files = [d for d in project_path.iterdir() if d.is_file()]
print(files)
ext = '.txt'
files_with_extension = [f for f in project_path.iterdir() if f.suffix == ext]
for i in files_with_extension:
    print(i.name)
    print(i.suffix)

current_work_directory = Path.cwd()
print("Поточна робоча директорія:", current_work_directory)
# new_directory = current_work_directory / "new_directory" / "dir"
# new_directory.mkdir(parents=True, exist_ok=True)