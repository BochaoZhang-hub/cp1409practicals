"""Module 2 - practical 2 """
import random

def main():
    score = float(input("Enter score: "))
    score_level = determine_score_level(score)
    print(f"Your score is {score}, your score level is {score_level}")
    score = random.randint(0,100)
    score_level = determine_score_level(score)
    print(f"Your random score is {score}, your score level is {score_level}")



def determine_score_level(score):
    """This function will determine score level based on what the score is."""
    if score < 0 or score > 100:
        return "invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"

main()