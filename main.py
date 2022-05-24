import random


def ask_player_to_choose():

    return int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Sicssors. ")
    )


def computer_choose():

    return random.randint(0, 2)


def compete(player, computer):

    truth_table = {
        (0, 0): "tie",
        (0, 1): "lost",
        (0, 2): "win",
        (1, 0): "win",
        (1, 1): "tie",
        (1, 2): "lost",
        (2, 0): "lost",
        (2, 1): "win",
        (2, 2): "tie",
    }

    return truth_table[(player, computer)]


def display(num):

    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

    paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

    print([rock, paper, scissors][num])


if __name__ == "__main__":

    player_pick = ask_player_to_choose()
    computer_pick = computer_choose()

    result = compete(player_pick, computer_pick)

    display(player_pick)

    print("Computer chose")

    display(computer_pick)

    print(f"You {result}")
