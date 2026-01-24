#import all the modules you need, below this line


#write any functions you need, below this line


#use the main() function for your program, define all other functions above main
def main ():
    #use print statements such as this one, to mark important points in the application, to help you with debugging
    print("Starting application...")

#please do not change the lines below, they are needed for your tests to work properly
#write all your code in the current file, and all your tests in the tests.py file
if __name__ == "__main__":
    main()

# 1. DEFINE FUNCTIONS ABOVE MAIN

def interpret_score(score):
    """
    Pure function to interpret total scores.
    Logic: High >= 12, Moderate 6-11, Low < 6.
    """
    if score >= 12:
        return "High"
    elif 6 <= score <= 11:
        return "Moderate"
    else:
        return "Low"

def get_valid_input(prompt):
    """
    Handles input validation and exception handling.
    Keeps asking until a valid number (0-7) is entered.
    """
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input) 
            if 0 <= value <= 7:
                return value
            else:
                print("⚠️ Error: Please enter a number between 0 and 7.")
        except ValueError:
            print("⚠️ Invalid input: Please enter a whole number (e.g., 5).")

# 2. THE MAIN FUNCTION
def main():
    print("Starting application...")
    
    # Data Structure: List of Dictionaries (15 Questions)
    questions = [
        # Category: SleepRoutine
        {"text": "Did you avoid caffeine in the late afternoon?", "habit": "SleepRoutine"},
        {"text": "Did you dim the lights 1 hour before sleep?", "habit": "SleepRoutine"},
        {"text": "Did you wake up at your goal time this morning?", "habit": "SleepRoutine"},
        
        # Category: PhysicalActivity
        {"text": "Did you take the stairs instead of the elevator?", "habit": "PhysicalActivity"},
        {"text": "Did you complete a dedicated workout session?", "habit": "PhysicalActivity"},
        {"text": "Did you stand or move around every hour today?", "habit": "PhysicalActivity"},
        
        # Category: HealthyEating
        {"text": "Did you include a source of protein in your meals?", "habit": "HealthyEating"},
        {"text": "Did you limit processed sugar or soda today?", "habit": "HealthyEating"},
        {"text": "Did you eat a variety of colorful vegetables?", "habit": "HealthyEating"},
        
        # Category: Mindfulness
        {"text": "Did you take 5 minutes for quiet reflection?", "habit": "Mindfulness"},
        {"text": "Did you focus on one task at a time (no multitasking)?", "habit": "Mindfulness"},
        {"text": "Did you spend time away from all digital notifications?", "habit": "Mindfulness"},
        
        # Category: SocialConnection
        {"text": "Did you have a face-to-face conversation today?", "habit": "SocialConnection"},
        {"text": "Did you reach out to someone just to check in?", "habit": "SocialConnection"},
        {"text": "Did you participate in a group activity or meal?", "habit": "SocialConnection"}
    ]

    # Initialize scores for the 5 categories
    category_scores = {
        "SleepRoutine": 0, "PhysicalActivity": 0, "HealthyEating": 0,
        "Mindfulness": 0, "SocialConnection": 0
        }

    print("\n--- Weekly Healthy Habits Quiz (15 Questions) ---")
    
    # Loop through questions and update scores
    for q in questions:
        answer = get_valid_input(f"Days per week - {q['text']}: ")
        category_scores[q['habit']] += answer

    # Display Results
    print("\n--- FINAL RESULTS ---")
    for habit, total in category_scores.items():
        interpretation = interpret_score(total)
        print(f"{habit}: Score {total} ({interpretation})")

# 3. RUN THE PROGRAM
if __name__ == "__main__":
    main()

    