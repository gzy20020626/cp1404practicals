"""
function main()
    print MENU
    get choice
    while choice != Q:
        if choice == G:
            get_valid_score()
        elif choice == P:
            result = convert_to_result(score)
            print result
        elif choice == S:
            print '*' * int(score)
        else:
            Invalid
    print "Thank you"
    
function get_valid_score()
    get score
    while score<0 or score>100:
        print invalid
        get score
        
function convert_to_result(score):
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    else:
        if score > 50:
            result = "Passable"
        if score > 90:
            result = "Excellent"
    if score < 50:
        result = "Bad"

    return result
"""

MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = convert_to_result(score)
            print(f"score:{score}, result:{result}")
        elif choice == 'S':
            print('*' * int(score))
        else:
            print("Invalid")

        print(MENU)
        choice = input(">>>").upper()

    print("Thank you!")


def get_valid_score():
    score = float(input("Entry your score, between 0 and 100: "))
    while score < 0 or score > 100:
        print("Invalid score!Re-entry!")
        score = float(input("Entry your score, between 0 and 100: "))
    return score


def convert_to_result(score):
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    else:
        if score > 50:
            result = "Passable"
        if score > 90:
            result = "Excellent"
    if score < 50:
        result = "Bad"

    return result


main()
