from os import system, name
import time
from Screen import Screen

class Score:

    screen = None

    def __init__(self):
        self.screen = Screen()

    def display_header(self, innings):
        self.screen.clear()

        innings.match.display_title()
        print("")
        
        print("-" * self.screen.width)
        print("")
        
        print("Innings of " + innings.batting_team.name)
        print("")

    def six(self, innings):
        self.screen.display_six_flash()
        print("")
        input("Press enter to continue")

    def four(self, innings):
        self.screen.display_four_flash()
        print("")
        input("Press enter to continue")

    def wicket(self, innings):
        self.screen.display_wicket_flash()
        print(innings.batter_on_strike.name + " is out, " + innings.current_ball.dismissal_type + "!")
        print("")
        input("Press enter to continue")

    def end_innings(self, innings):
        self.display_header(innings)
        print("Innings score: " + str(innings.runs) + " / " + str(innings.wickets) + " (" + str(innings.current_over_number) + " overs)")
        print("")
        input("Press enter to continue")

    def update_scoreboard(self, innings):
        self.display_header(innings)
        
        print(str(innings.runs) + " / " + str(innings.wickets) + " (" + str(innings.current_over_number) + "." + str(innings.current_ball_number) + " overs)")
        print("")
        
        print(innings.batter_on_strike.name + " * (" + str(innings.batter_on_strike.batting_stats.runs) + " off " + str(innings.batter_on_strike.batting_stats.balls) + ")")
        print(innings.batter_off_strike.name + " (" + str(innings.batter_off_strike.batting_stats.runs) + " off " + str(innings.batter_off_strike.batting_stats.balls) + ")")
        print("")

        print("Over " + str(innings.current_over_number + 1))
        print("Bowler: " + innings.bowler.name)
        print(innings.current_over.get_over_stats())
        print("")


