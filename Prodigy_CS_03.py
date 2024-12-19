import re

def password_strength_checker(password):
    # Criteria weights
    length_weight = 2
    complexity_weight = 3
    digit_weight = 1
    special_char_weight = 1

    # Scoring variables
    score = 0

    # Length check
    if len(password) >= 12:
        score += length_weight
    elif len(password) >= 8:
        score += 1

    # Complexity check
    if (any(char.isupper() for char in password) and 
        any(char.islower() for char in password) and 
        any(char.isdigit() for char in password) and 
        any(not char.isalnum() for char in password)):
        score += complexity_weight

    # Digit check
    if any(char.isdigit() for char in password):
        score += digit_weight

    # Special character check
    if any(not char.isalnum() for char in password):
        score += special_char_weight

    return score

def password_strength_feedback(score):
    if score >= 7:
        return "Strong Password! Excellent job!"
    elif score >= 5:
        return "Good Password! Keep it up!"
    elif score >= 3:
        return "Fair Password. Try to make it stronger."
    else:
        return "Weak Password. Please choose a stronger Password."

def main():
    password = input("Enter your Password: ")
    strength_score = password_strength_checker(password)
    feedback = password_strength_feedback(strength_score)
    print("Password strength score:", strength_score)
    print("Feedback:", feedback)

if __name__ == "__main__":
    main()