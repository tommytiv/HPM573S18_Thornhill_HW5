from enum import Enum
import numpy as np
import scr.FigureSupport as Fig


class CoinToss(Enum):  # State of each coin toss
    HEADS = 1
    TAILS = 0


class Game:  # create cointoss game
    def __init__(self):
        self._rnd = np.random  # generate random number for coin flip
        self._headProb = head_prob  # probability of getting Heads
        self._CoinToss = []  # outcome of toss
        self._results = []  # outcome of all tosses in a Game

    def simulate(self, tosses):
        t = 0  # first toss
        while t < tosses:  # while number of tosses has not been reached
            if self._rnd.sample() < self._headProb:  # odds of getting heads
                self._CoinToss = CoinToss.HEADS
            else:
                self._CoinToss = CoinToss.TAILS  # if not heads, then tails
            self._results.append(self._CoinToss.name)  # create list of results
            t += 1  # repeat toss
            # print (t) #to check number of tosses

    def tally(self):
        countable = " ".join(map(str, self._results))
        wins = countable.count(winning_sequence)
        total = -entry_fee + (wins * reward)
        # print (countable) # TO CHECK for number of tosses
        # print (wins) # TO CHECK number of tosses
        # print (total) # TO CHECK total
        return total


class Rounds:
    def __init__(self, rounds):
        self.initialRounds = rounds
        self.games = []
        self.total_tally = []

        for i in range(rounds):  # to iterate through rounds
            game = Game()  # game is an instance of Game
            self.games.append(game)  # create a list of games to append the talliies

    def play(self):
        for game in self.games:
            game.simulate(n_tosses)  # initiate cointoss
            outcome = game.tally()
            self.total_tally.append(outcome)

    def get_total_tally(self):  # creates a list of the vakue of each round
        return self.total_tally

    def get_avg_tally(self):  # returns the average value
        return sum(self.total_tally) / len(self.total_tally)

    def get_min_tally(self):  # returns the minimum value
        return min(self.total_tally)

    def get_max_tally(self):  # returns the maximum value
        return max(self.total_tally)

    def get_probability_of_loss(self):  # returns the proportion of rounds with a value less than 0
        return sum(i < 0 for i in self.total_tally) / num_rounds


# Values of constants
head_prob = 0.5
n_tosses = 20
num_rounds = 1000
entry_fee = 250
reward = 100
winning_sequence = "TAILS TAILS HEADS"

myRounds = Rounds(num_rounds)  # Create rounds
myRounds.play()  # Play rounds
print("Expected value:", myRounds.get_avg_tally())
print("Probability of loss:", myRounds.get_probability_of_loss())
print("\n")
print("Minimum value:", myRounds.get_min_tally())
print("Minimum possible value:", -entry_fee)
print("Maximum value:", myRounds.get_max_tally())
print("Maximum possible value: 350")
print("\n")
print("Based on a coin toss game with the following parameters:")
print("Probability of getting Heads:", head_prob)
print("Number of coin tosses per game:", n_tosses)
print("Number of rounds of games:", num_rounds)
print("Entry fee to play each game:", entry_fee)
print("Reward for each winning sequence:", reward)
print("Winning sequence:", winning_sequence)

# plot the histogram
Fig.graph_histogram(
    observations=myRounds.get_total_tally(),
    title='Histogram of Rewards',
    x_label='Rewards ($)',
    y_label='Rounds')
