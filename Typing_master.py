import random
import time
import sys
import json

# Define a dictionary of programming languages with associated word lists.
programming_languages = {
    "C": ["function", "pointer", "variable", "compiler", "library"],
    "Python": ["python", "programming", "challenge", "coding", "keyboard"],
    "Java": ["java", "programming", "language", "class", "method"],
    "JavaScript": ["javascript", "web", "frontend", "function", "variable"],
    "Ruby": ["ruby", "rails", "gem", "method", "class"],
    "C++": ["cplusplus", "object", "oriented", "inheritance", "polymorphism"],
    "Go": ["golang", "concurrency", "goroutine", "channel", "slices"],
    "C#": ["csharp", "interface", "property", "delegate", "namespace"],
    "TypeScript": ["typescript", "types", "interface", "compiler", "module"],
    "Rust": ["rust", "safety", "ownership", "lifetime", "borrowing"]
}

def update_leaderboard(leaderboard, username, wpm):
    leaderboard.append({"username": username, "wpm": wpm})
    leaderboard.sort(key=lambda x: x["wpm"], reverse=True)
    if len(leaderboard) > 10:
        leaderboard.pop()
    return leaderboard

def show_leaderboard(leaderboard):
    print("\nLeaderboard:")
    if not leaderboard:
        print("No records yet.")
    else:
        for i, entry in enumerate(leaderboard, 1):
            print(f"{i}. {entry['username']} - {entry['wpm']} WPM")

def main():
    leaderboard_file = "leaderboard.json"
    leaderboard = []

    username = input("Enter your username: ")

    while True:
        print("\n1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nChoose a programming language:")
            for i, language in enumerate(programming_languages, 1):
                print(f"{i}. {language}")

            language_choice = input("Enter the number for your chosen language: ")

            if language_choice.isdigit() and 1 <= int(language_choice) <= len(programming_languages):
                language_name = list(programming_languages.keys())[int(language_choice) - 1]
                words_to_type = programming_languages[language_name]

                print(f"Start Typing Test for {language_name} language.")

                start_time = time.time()
                words_typed = 0

                while True:
                    word = random.choice(words_to_type)
                    print(f"Type: {word}")
                    user_word = input("Your word: ")

                    if user_word.lower() == "ctrl + q":
                        print("Typing test aborted.")
                        break

                    if user_word == word:
                        words_typed += 1
                    else:
                        print("Incorrect word. Try again.")

                end_time = time.time()
                time_taken = end_time - start_time
                wpm = int(words_typed / (time_taken / 60))

                print(f"\nTyping Test Results for {username}:")
                print(f"Words Typed: {words_typed}")
                print(f"Time Taken: {time_taken:.2f} seconds")
                print(f"Words Per Minute (WPM): {wpm}")

                leaderboard = update_leaderboard(leaderboard, username, wpm)
                with open(leaderboard_file, 'w') as file:
                    json.dump(leaderboard, file, indent=2)

            else:
                print("Invalid language choice. Please select a number from 1 to 10.")

        elif choice == "2":
            show_leaderboard(leaderboard)

        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            sys.exit()

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()