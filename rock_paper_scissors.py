import random



def who_wins(user, computer):
    if user == computer:
        result = "It is a tie"
    else:
        if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            result = "You win!"
        else:
            result = "The computer wins"
    return result

def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    else:
        if choice == 2:
            return "Paper"
        else:
            if choice == 3:
                return "Scissors"
            else:
                return "Invalid choice"

def main():
    user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
    computer_choice = random.randint(1, 3)

    print("You chose: ", get_choice_name(user_choice))
    print("Computer chose: ", get_choice_name(computer_choice))

    result = who_wins(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()
