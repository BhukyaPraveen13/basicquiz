class QuizGame:
    def __init__(self, questions):
        self.questions = questions  # Store quiz questions for selected level
        self.score = 0  # Initialize the score
    
    def ask_question(self, question_data):
        """
        Function to display each question and handle user input.
        It validates the input and ensures it's a valid choice.
        """
        print(f"\n{question_data['question']}")
        for choice in question_data['choices']:
            print(choice)

        # Get user input with validation for choices
        user_answer = input("\nEnter your answer (A, B, C, or D): ").upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            print("Invalid choice. Please select A, B, C, or D.")
            user_answer = input("\nEnter your answer (A, B, C, or D): ").upper()
        
        return user_answer

    def give_feedback(self, user_answer, correct_answer):
        """
        Function to provide feedback after each answer.
        """
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1  # Increase score for correct answer
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    def show_final_score(self):
        """
        Function to display the final score and performance feedback.
        """
        total_questions = len(self.questions)
        print(f"\nGame Over! You answered {self.score} out of {total_questions} questions correctly.")
        percentage = (self.score / total_questions) * 100
        print(f"Your score: {percentage}%")

        if percentage == 100:
            print("Excellent! You got all the answers correct!")
        elif percentage >= 80:
            print("Great job!")
        elif percentage >= 50:
            print("Good effort! But there's room for improvement.")
        else:
            print("Keep practicing! You'll get better.")

    def run(self):
        """
        Main function to run the quiz.
        It iterates over the questions, calls relevant functions, and tracks the score.
        """
        print("Welcome to the Basic Quiz Game!\n")
        for question_data in self.questions:
            user_answer = self.ask_question(question_data)
            self.give_feedback(user_answer, question_data['answer'])

        self.show_final_score()


# Function to create quiz data (easy, medium, hard)
def get_quiz_data(level):
    if level == 'easy':
        return [
            {
                "question": "What is the capital of France?",
                "choices": ["A) Paris", "B) Berlin", "C) Madrid", "D) Rome"],
                "answer": "A"
            },
            {
                "question": "What is 2 + 2?",
                "choices": ["A) 3", "B) 4", "C) 5", "D) 6"],
                "answer": "B"
            },
            {
                "question": "Which planet is closest to the Sun?",
                "choices": ["A) Mercury", "B) Venus", "C) Earth", "D) Mars"],
                "answer": "A"
            }
        ]
    
    elif level == 'medium':
        return [
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "choices": ["A) Shakespeare", "B) Dickens", "C) Austen", "D) Tolstoy"],
                "answer": "A"
            },
            {
                "question": "Which programming language is known as the 'language of the web'?",
                "choices": ["A) Python", "B) JavaScript", "C) Java", "D) C++"],
                "answer": "B"
            },
            {
                "question": "Which is the largest continent by area?",
                "choices": ["A) Africa", "B) Asia", "C) Europe", "D) North America"],
                "answer": "B"
            }
        ]

    elif level == 'hard':
        return [
            {
                "question": "Who developed the theory of relativity?",
                "choices": ["A) Isaac Newton", "B) Albert Einstein", "C) Nikola Tesla", "D) Galileo"],
                "answer": "B"
            },
            {
                "question": "Which planet has the most moons in our Solar System?",
                "choices": ["A) Jupiter", "B) Saturn", "C) Uranus", "D) Neptune"],
                "answer": "B"
            },
            {
                "question": "What is the atomic number of Uranium?",
                "choices": ["A) 92", "B) 82", "C) 72", "D) 62"],
                "answer": "A"
            }
        ]

# Main function to select difficulty level and run the game
def start_game():
    print("Select your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    level_choice = input("Enter 1, 2, or 3: ").strip()
    
    if level_choice == '1':
        level = 'easy'
    elif level_choice == '2':
        level = 'medium'
    elif level_choice == '3':
        level = 'hard'
    else:
        print("Invalid choice. Defaulting to 'easy'.")
        level = 'easy'
    
    quiz_data = get_quiz_data(level)  # Get the questions based on the selected level
    quiz_game = QuizGame(quiz_data)  # Create the QuizGame object
    quiz_game.run()  # Start the quiz


# Run the game
if __name__ == "__main__":
    start_game()
