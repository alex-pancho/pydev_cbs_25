import csv
from pathlib import Path


def read_file(filepath: Path) -> list:
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        # if not rows:
        #     return []
        
        # # First row contains headers
        # headers = rows[0]
        
        # # Convert remaining rows to dictionaries
        # result = []
        # for row in rows[1:]:
        #     # Handle rows with different lengths than headers
        #     row_dict = {}
        #     for i, header in enumerate(headers):
        #         row_dict[header] = row[i] if i < len(row) else ""
        #     result.append(row_dict)
        
        return rows

def write_csv(filepath: Path, content: list):
    if not content:
        return
    
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        
        # Extract headers from first dictionary
        headers = list(content[0].keys())
        writer.writerow(headers)
        
        # Write data rows
        for row_dict in content:
            row = [row_dict.get(header, "") for header in headers]
            writer.writerow(row)


if __name__ == "__main__":
    my_csv = Path(__file__).parent / "users_1.csv"
    content = read_file(my_csv)
    print(content, type(content))
    # my_csv_2 = Path(__file__).parent / "new2.csv"
    # write_csv(my_csv_2, content)