"""Module 2 - practical 2 """

def main():
    """this function will display the menu"""
    score = -1
    menu = """
    This is a score menu.
    (G)et a valid score 
    (P)rint result 
    (S)how stars
    (Q)uit    
    """
    print(menu)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(score)
        elif choice == "P":
            score = check_score(score)
            score_level = determine_score_level()
            print(f"your score level is {score_level}")
        elif choice == "S":
            score = check_score(score)
            show_stars(score)
        else:
            print("invalid choice")
        print(menu)
        choice = input("Enter your choice: ").upper()
    print("Goodbye! Thanks for using and hope to see you next time!")

def get_valid_score():
    """This function will validate the number input."""
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        score = float(input("Enter your score again, your input is invalid: "))
    return score

def show_stars(score):
    """This function will display the stars."""
    print("*"*score)

def determine_score_level(score):
    """This function will determine score level based on what the score is."""
    if score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    else:
        return "bad"

def check_score(score):
    """This function will check if the score is still default."""
    if score == -1:
        score = float(input("Enter your score: "))
    return score
main()