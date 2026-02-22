import os
import argparse

from default_definitions import DEFAULT_DATA_CSV_PATH
from utilities.control_csv import append_to_csv

def add_sentence(csv_path: str):
    jp_en_list = []
    while True:
      jp = input("日本語: ").strip()
      en = input("English: ").strip()

      if not jp or not en:
          print("❌ 日本語と英語は必須です")
          continue

      jp_en_list.append((jp, en))
      next_command=input("✅ 追加しました。続けて入力するか、'q'を入力して終了してください。")
      if next_command.lower() == "q":
        break

    if not os.path.exists(csv_path):
      print("❌ CSV file not found.")
      return
      
    append_to_csv(csv_path, jp_en_list)

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