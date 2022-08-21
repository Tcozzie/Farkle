import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 12
# November 16, 2021
# Tiegan Cozzie
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die with given number of sides"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Farkle:

    def __init__(self, sides):
        """A constructor method that can record 6 dice rolls"""
        self.rolls = np.zeros(6, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 6 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts
        
#--------------------------------------------------

    def is_it_four_of_a_kind(self):
       counts=self.count_outcomes()
       for  x in counts:
           if x==4:
               return True
        
    def is_it_straight(self):
        num=np.sort(self.rolls)
        count=0
        check=0
        for x in range(len(num)):
            if num[0]+count==num[x]:
                check+=1
            else:
                check=check
            count+=1
        if check==6:
            return True
    
    def is_it_two_triplets(self):
        counts=self.count_outcomes()
        count=0
        for x in counts:
            if x==3:
                count+=1
            else:
                count=count
        if count==2:
            return True

# -------------------------------------------------
        
def main(how_many):

    four_of_a_kind = 0
    straight = 0
    two_triplets = 0
    game = Farkle(6)

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_four_of_a_kind():
            four_of_a_kind += 1
        elif game.is_it_straight():
            straight += 1
        elif game.is_it_two_triplets():
            two_triplets += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    
    print("Number of Four of a Kinds:", four_of_a_kind)
    print("Apparent Probability: 1 in {:.2f}\n".format(how_many/four_of_a_kind))
    print("Number of Straights:", straight)
    print("Apparent Probability: 1 in {:.2f}\n".format(how_many/straight))
    print("Number of Two Triplets:", two_triplets)
    print("Apparent Probability: 1 in {:.2f}\n".format(how_many/two_triplets))

# -------------------------------------------------

main(1000)
    
        
