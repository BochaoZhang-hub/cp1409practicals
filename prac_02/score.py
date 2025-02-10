"""Module 2 - practical 2 """
import random

def main():
    score = get_number()
    score_level = determine_score_level(score)
    print(f"Your score is {score}, your score level is {score_level}")
    score = random.randint(0,100)
    score_level = determine_score_level(score)
    print(f"Your random score is {score}, your score level is {score_level}")


def get_number():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Please enter a number between 0 and 100")
        score = float(input("Enter score: "))
    return score

def determine_score_level(score):
    """This function will determine score level based on what the score is."""
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"

main()