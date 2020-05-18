#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time  # https://www.tutorialspoint.com/python/time_sleep.htm
moves = ['rock', 'paper', 'scissors']  # all possible moves

"""The Player class is the parent class for all of the Players
in this game"""


class Player:  # count wins, set player variables, report moves
    wins = 0
    my_move = ""
    their_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):  # Random player with random moves
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):  # Ask for input and check validity
    def move(self):
        the_player_input = input("Choose paper,"
                                 "rock or scissors: ")
        if the_player_input in moves:
            return the_player_input
        else:
            print("The choice you made is invalid,"
                  " please enter rock, paper or scissors")
            time.sleep(1)
            self.move()


class ReflectPlayer(Player):  # Remember opponent previous play and mirror
    def move(self):
        if self.their_move in moves:
            return self.their_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):  # Cycle to next play from previous
    def move(self):
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"
        else:
            return random.choice(moves)


def beats(one, two):  # Set rules
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:  # Set player and round rules and print outcome
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 played: {move1}  Player 2 played: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1.wins += 1
            time.sleep(1)
            print(f"PLAYER 1 WINS THE ROUND {self.p1.wins}"
                  f" to {self.p2.wins}")
        elif beats(move2, move1):
            self.p2.wins += 1
            time.sleep(1)
            print(f"PLAYER 2 WINS THE ROUND {self.p2.wins}"
                  f" to {self.p1.wins}")
        else:
            time.sleep(1)
            print(f"IT'S A TIE! THE SCORE IS {self.p1.wins}"
                  f" to {self.p2.wins}")

    def play_game(self):
        print("Let's play!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        time.sleep(1)
        if self.p1.wins > self.p2.wins:
            print(f"Player 1 wins the game with a score of {self.p1.wins}"
                  f" to {self.p2.wins}")
        elif self.p2.wins > self.p1.wins:
            print(f"Player 2 wins the game with a score of {self.p2.wins}"
                  f" to {self.p1.wins}")
        else:
            print(f"Nobody wins. Both players "
                  f"have the score of {self.p1.wins}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
