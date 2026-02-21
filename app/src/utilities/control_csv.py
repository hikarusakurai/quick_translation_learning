import csv

def load_csv_file(file_path: str):
    with open(file_path, newline="", encoding="utf-8") as f:
        data = csv.reader(f)
        return list(data)
    

def append_to_csv(csv_path: str, jp_en_list: list):
    with open(csv_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for jp, en in jp_en_list:
            writer.writerow([jp, en])