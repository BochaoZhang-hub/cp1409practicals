"""Module 2 - practical 2 """

def main():
    menu = """
    This is a score menu.
    (G)et a valid score 
    (P)rint result 
    (S)how stars
    (Q)uit    
    """
    print(menu)
    score = int(input("Enter your score: "))
    score = get_valid_score(score)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(score)
        elif choice == "P":
            score_level = determine_score_level(score)
            print(f"your score level is {score_level}")
        elif choice == "S":
            show_stars(score)
        else:
            print("invalid choice")
            choice = input("Enter your choice: ").upper()
        print(menu)
        choice = input("Enter your choice: ").upper()
    print("Goodbye! Thanks for using and hope to see you next time!")

def get_valid_score(score):
    """This function will validate the number input."""
    while score < 0 or score > 100:
        score = int(input("Enter your score again, your input is invalid: "))
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
main()