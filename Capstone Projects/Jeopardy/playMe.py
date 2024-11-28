import pandas as pd
import random

# Load the dataset
questions = pd.read_csv('jeopardy.csv')

# Clean column names and drop rows with missing values
questions.columns = questions.columns.str.strip()
questions = questions.dropna(subset=['Question', 'Answer'])
def quiz_yourself(df):
    """
    Runs a quiz system for the user to answer random questions.

    Parameters:
        df (pd.DataFrame): The dataset.

    Returns:
        None
    """
    print("Welcome to the Jeopardy Quiz!")
    correct_count = 0
    total_questions = 5  # Number of questions to ask

    try:
        # Ask random questions
        for _ in range(total_questions):
            question = df.sample(1).iloc[0]  # Randomly select a question
            print("\nQuestion:")
            print(question['Question'])
            user_answer = input("Your answer: ")

            # Check correctness
            if user_answer.strip().lower() == question['Answer'].strip().lower():
                print("Correct!")
                correct_count += 1
            else:
                print(f"Wrong. The correct answer was: {question['Answer']}")

    except KeyboardInterrupt:
        print("\nQuiz Interrupted. Exiting...")
        return

    # Quiz summary
    print("\nQuiz Complete!")
    print(f"You got {correct_count} out of {total_questions} questions right.")

# Run the quiz system
quiz_yourself(questions)

