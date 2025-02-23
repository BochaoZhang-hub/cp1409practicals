import random
from unittest import load_tests


def main():
    """This function will generate a lottery"""
    MAX_NUMBER = 45
    MIN_NUMBER = 1
    NUMBERS_EVERYTIME = 6
    print_sorted_lottery(MAX_NUMBER, MIN_NUMBER, NUMBERS_EVERYTIME)


def print_sorted_lottery(MAX_NUMBER, MIN_NUMBER, NUMBERS_EVERYTIME):
    """This function will generate all the draws the user want"""
    numbers_of_picks = int(input("how many quick picks?"))
    for i in range(numbers_of_picks):
        lottery_samples = []
        for j in range(NUMBERS_EVERYTIME):
            lottery_samples.append(random.randint(MIN_NUMBER, MAX_NUMBER))
        lottery_samples.sort()
        print(" ".join(f"{sample:>2}" for sample in lottery_samples))


main()