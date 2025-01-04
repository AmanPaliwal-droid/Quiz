import os

# Read questions from questions.txt
def load_questions():
    questions = []
    if os.path.exists("questions.txt"):
        with open("questions.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                question = parts[0]
                options = parts[1:5]
                correct_answer = parts[5]
                questions.append((question, *options, correct_answer))
    return questions

# Function to conduct the quiz
def start_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question[0]}")
        print(f"A. {question[1]}")
        print(f"B. {question[2]}")
        print(f"C. {question[3]}")
        print(f"D. {question[4]}")
        
        answer = input("Your Answer: ").upper()

        # Validate the answer
        if answer in ['A', 'B', 'C', 'D'] and answer == question[5]:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was {question[5]}.\n")
    
    return score

# Save the score to scores.txt
def save_score(name, score, total_questions):
    with open("scores.txt", "a") as file:
        file.write(f"{name},{score}/{total_questions}\n")
    print("Your score has been saved!")

# Main program
def main():
    print("Welcome to the Quiz Application!")
    print("Rules:")
    print("- Each question has 4 options.")
    print("- Enter the option (A, B, C, D) as your answer.")
    input("Press Enter to Start!\n")
    
    questions = load_questions()
    
    if not questions:
        print("No questions available. Please check questions.txt file.")
        return

    score = start_quiz(questions)
    print(f"Quiz Complete! Your Score: {score}/{len(questions)}")
    
    name = input("Enter your name: ")

    # Save the score
    save_score(name, score, len(questions))

if __name__ == "__main__":
    main()
