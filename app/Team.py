import random
from Randomiser import Randomiser
from Score import Score

class Team:

    name = None
    squad = None
    score = None

    def __init__(self, name, gender):
        rand = Randomiser()
        
        self.name = name
        self.score = Score()

        self.squad = []
        for i in range(11):
            player = rand.get_player(gender)
            player.number = i + 1
            self.squad.append(player)

        self.squad[random.randint(0, 10)].captain = True
        self.squad[random.randint(0, 10)].wicket_keeper = True

    def print_squad(self):
        for player in self.squad:
            captain = " (C)" if player.captain else ""
            wicket_keeper = " (WK)" if player.wicket_keeper else ""
            print(str(player.number) + ": " + player.name + captain + wicket_keeper)

    def print_name(self):
        print(self.name)