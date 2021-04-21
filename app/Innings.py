import time
from Over import Over
from Randomiser import Randomiser

class Innings:

    match = None
    batting_team = None
    bowling_team = None
    batter_on_strike = None
    batter_off_strike = None
    bowler = None
    overs = None
    current_over = None
    current_over_number = 0
    current_ball = None
    current_ball_number = 0
    runs = 0
    wickets = 0
    randomiser = None

    def __init__(self, match, batting_team, bowling_team, overs):
        self.match = match
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.overs = overs
        self.current_ball_number = 0
        self.current_over_number = 0
        self.runs = 0
        self.wickets = 0
        self.randomiser = Randomiser()

    def update_scoreboard(self):
        self.match.score.update_scoreboard(self)

    def swap_ends(self):
        old_batter_on_strike = self.batter_on_strike
        self.batter_on_strike = self.batter_off_strike
        self.batter_off_strike = old_batter_on_strike

    def start(self):
        
        innings_ended = False

        self.batter_on_strike = self.batting_team.squad[0]
        self.batter_off_strike = self.batting_team.squad[1]
        next_batter = 2

        self.bowler = self.randomiser.get_next_bowler(self.bowling_team, self.bowler)

        while innings_ended == False:

            # make sure we only play the right number of overs
            if self.current_over_number >= self.overs:
                return
            
            self.current_over = None
            self.current_over = Over(self.current_over_number)
            self.update_scoreboard()

            for self.current_ball_number in range(1, 7):

                input("Press enter to bowl...")

                self.current_ball = self.current_over.get_ball(self.current_ball_number)

                self.batter_on_strike.batting_stats.balls += 1

                # the batter is out, fetch the next one
                if self.current_ball.result == "W":
                    next_batter += 1
                    self.batter_on_strike.batting_stats.how_out = self.current_ball.dismissal_type
                    # if that was the 10th batter out, finish the innings
                    if next_batter == 10:
                        innings_ended = True
                        self.match.score.end_innings(self)
                        break
                    self.match.score.wicket(self)
                    self.wickets += 1
                    self.batter_on_strike = self.batting_team.squad[next_batter]

                if self.current_ball.runs > 0:
                    if self.current_ball.runs == 6:
                        self.match.score.six(self)
                    if self.current_ball.runs == 4:
                        self.match.score.four(self)
                    self.batter_on_strike.batting_stats.runs += self.current_ball.runs
                    self.runs += self.current_ball.runs

                if self.current_ball.batters_swapped:
                    self.swap_ends()

                self.update_scoreboard()

            # next over
            self.current_ball_number = 0
            self.current_over_number += 1
            self.update_scoreboard()
            self.bowler = self.randomiser.get_next_bowler(self.bowling_team, self.bowler)
            self.swap_ends()
            input("Press enter to start the next over...")