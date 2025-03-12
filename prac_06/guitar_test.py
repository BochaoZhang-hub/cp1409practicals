from guitar import Guitar

def test_get_age():
    """this function will test if we get the guitar correctly"""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00)

    print(f"{guitar1.name} get_age() - Expected 103. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 12. Got {guitar2.get_age()}")

def test_is_vintage():
    """this function will test if its vintage"""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1200.00)

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

test_get_age()
test_is_vintage()
