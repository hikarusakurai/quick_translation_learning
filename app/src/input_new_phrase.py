import csv
import os
import argparse

from default_definitions import DEFAULT_DATA_CSV_PATH
from utilities.control_csv import append_to_csv

def add_sentence(csv_path: str):
    jp_en_list = []
    while True:
      jp = input("日本語: ").strip()
      en = input("English: ").strip()

      if jp.lower() == "q" or en.lower() == "q":
          break

      if not jp or not en:
          print("❌ 日本語と英語は必須です")
          continue

      jp_en_list.append((jp, en))

    if not os.path.exists(csv_path):
      print("❌ CSV file not found.")
      return
      
    append_to_csv(csv_path, jp_en_list)
    
    print("✅ 追加しました")

def main():
    parser = argparse.ArgumentParser(
        description="Instant English - Quick Translation Learning"
    )
    parser.add_argument(
        "--input_file_path",
        type=str,
        default=DEFAULT_DATA_CSV_PATH,
        help="Path of CSV file containing Japanese and English sentences"
    )
    args = parser.parse_args()

    add_sentence(args.input_file_path)

if __name__ == "__main__":
    main()