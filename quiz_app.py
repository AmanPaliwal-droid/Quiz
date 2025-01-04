import os
import datetime

def load_questions(file_name):
    questions = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 6:
                    questions.append({
                        "question": parts[0],
                        "options": parts[1:5],
                        "answer": parts[5]
                    })
    except FileNotFoundError:
        print(f"Error: {file_name} not found!")
    return questions

def conduct_quiz(questions):
    score = 0
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q['options'], start=1):
            print(f"  {chr(64+j)}. {option}")
        answer = input("Your Answer (A, B, C, D): ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct Answer: {q['answer']}")
    return score, len(questions)

def save_score(file_name, user_name, score, total):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    try:
        with open(file_name, "a") as file:
            file.write(f"{user_name}, {score}/{total}, {date}\n")
    except Exception as e:
        print(f"Error saving score: {e}")

def main():
    print("Welcome to the Quiz Application!")
    questions_file = "questions.txt"
    scores_file = "scores.txt"
    
    questions = load_questions(questions_file)
    if not questions:
        print("No questions available. Exiting...")
        return

    user_name = input("Enter your name: ")
    score, total = conduct_quiz(questions)
    print(f"\nQuiz Complete! Your Score: {score}/{total}")
    save_score(scores_file, user_name, score, total)
    print(f"Score saved to {scores_file}!")

if __name__ == "__main__":
    main()
