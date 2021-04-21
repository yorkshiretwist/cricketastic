import time
from Over import Over
from Randomiser import Randomiser

class Innings:

    match = None
    batting_team = None
    bowling_team = None
    batter_on_strike = None
    batter_off_strike = None
    next_batter_index = 0
    bowler = None
    overs = None
    current_over = None
    current_over_number = 0
    current_ball = None
    current_ball_number = 0
    randomiser = None

    def __init__(self, match, batting_team, bowling_team, overs):
        self.match = match
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.batter_on_strike = None
        self.batter_off_strike = None
        self.next_batter_index = 0
        self.bowler = None
        self.overs = overs
        self.current_over = None
        self.current_over_number = 0
        self.current_ball = None
        self.current_ball_number = 0
        self.randomiser = Randomiser()

    def swap_ends(self):
        old_batter_on_strike = self.batter_on_strike
        self.batter_on_strike = self.batter_off_strike
        self.batter_off_strike = old_batter_on_strike

    def start(self):
        
        innings_ended = False

        self.batter_on_strike = self.batting_team.squad[0]
        self.batter_off_strike = self.batting_team.squad[1]
        self.next_batter_index = 2

        self.bowler = self.randomiser.get_next_bowler(self.bowling_team, self.bowler)

        while innings_ended == False:

            # make sure we only play the right number of overs
            if self.current_over_number >= self.overs:
                self.batting_team.score.innings_completed = True
                self.match.scoreboard.end_innings(self)
                return
            
            self.current_over = None
            self.current_over = Over(self.current_over_number)
            self.match.scoreboard.update(self)

            for self.current_ball_number in range(1, 7):
                play_next_ball = self.play_ball()                
                if play_next_ball == False:
                    innings_ended = True
                    break

            # next over
            self.current_ball_number = 0
            self.current_over_number += 1
            self.match.scoreboard.update(self)
            self.bowler = self.randomiser.get_next_bowler(self.bowling_team, self.bowler)
            self.swap_ends()
            if self.current_over_number < self.overs:
                input("Press enter to start the next over...")

        # complete the innings
        self.batting_team.score.innings_completed = True
        self.match.scoreboard.end_innings(self)

    def play_ball(self):
        input("Press enter to bowl...")

        self.current_ball = self.current_over.get_ball(self.current_ball_number)

        self.batter_on_strike.batting_stats.balls += 1

        # the batter is out
        if self.current_ball.result == "W":
            self.next_batter_index += 1
            # store how the batter was out
            self.batter_on_strike.batting_stats.how_out = self.current_ball.dismissal_type
            # if that was the 10th batter out, finish the innings
            if self.next_batter_index == 10:
                self.match.scoreboard.end_innings(self)
                return False
            # trigger the wicket UI
            self.match.scoreboard.wicket(self)
            # update the batting team score
            self.batting_team.score.wickets += 1
            # fetch the next batter
            self.batter_on_strike = self.batting_team.squad[self.next_batter_index]

        # if this was a scoring ball
        if self.current_ball.runs > 0:
            # trigger the 6 or 4 UI
            if self.current_ball.runs == 6:
                self.match.scoreboard.six(self)
            if self.current_ball.runs == 4:
                self.match.scoreboard.four(self)
            # update the batter stats
            self.batter_on_strike.batting_stats.runs += self.current_ball.runs
            # update the batting team score
            self.batting_team.score.runs += self.current_ball.runs

        if self.current_ball.batters_swapped:
            self.swap_ends()

        self.match.scoreboard.update(self)
        return True