from BattingStats import BattingStats

class Player:

    name = None
    number = 0
    captain = False
    wicket_keeper = False
    batting_stats = None
    bowling_stats = None

    def __init__(self, name):
        self.name = name
        self.batting_stats = BattingStats()