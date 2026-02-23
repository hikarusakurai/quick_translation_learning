import random
import time
import argparse
import os

from default_definitions import DEFAULT_DATA_CSV_PATH, DEFAULT_TIME_LIMIT, MAX_QUESTIONS
from utilities.control_csv import load_csv_file


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def run_quick_translation_learning(data: list, time_limit: float=DEFAULT_TIME_LIMIT, max_questions: int=MAX_QUESTIONS):
    # shuffle data for random order
    random.shuffle(data)

    # run the quiz and collect slow questions
    slow_questions = []
    for i, (jp, en) in enumerate(data):
        clear_screen()
        num_q=i+1
        print("\n==============================")
        print(f"Question-{num_q}")
        print("Japanese：", jp)

        start = time.perf_counter()
        input("▶ 英語を言ったら Enter: ")
        elapsed = time.perf_counter() - start

        print("English：", en)
        print(f"⏱ {elapsed:.2f} sec")

        if elapsed > time_limit:
            print("⚠️ Time over!!")
            slow_questions.append((jp, en))

        next_command = input("▶ Next! Press Enter or type 'q' to quit: ")
        if next_command.lower() == "q":
            print("👋 Goodbye!")
            exit(0) 
        if num_q >= max_questions:
            break

    return slow_questions

def quick_translation_learning(file_path: str, time_limit: float = 1.5, max_questions: int = 50):
    rows = load_csv_file(file_path)

    if len(rows) < 2:
        print("Please put correct data")
        return

    _, question_list = rows[0], rows[1:]

    clear_screen()
    input("▶ Are you ready? Press Enter to start.")
    loop_count = 0
    while question_list:
        if loop_count > 1:
            print("\n🔁 Let's try the slow questions again!")
        question_list = run_quick_translation_learning(question_list, time_limit, max_questions)
        loop_count += 1

    print("\n✅ 全ての問題をクリア！お疲れ様でした！")


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
    parser.add_argument(
        "--time_limit",
        type=float,
        default=DEFAULT_TIME_LIMIT,
        help="Time limit in seconds"
    )
    parser.add_argument(
        "--max_questions",
        type=int,
        default=MAX_QUESTIONS,
        help="Maximum number of questions per round"
    )

    args = parser.parse_args()

    start = time.perf_counter()
    quick_translation_learning(
        file_path=args.input_file_path,
        time_limit=args.time_limit,
        max_questions=args.max_questions
    )
    minutes = (time.perf_counter() - start) / 60
    seconds = (time.perf_counter() - start) % 60
    print(f"⏱ Total time: {int(minutes)} min {int(seconds)} sec")
    

if __name__ == "__main__":
    main()