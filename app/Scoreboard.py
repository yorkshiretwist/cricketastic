from os import system, name
import time
from Screen import Screen

class Scoreboard:

    screen = None

    def __init__(self):
        self.screen = Screen()

    def header(self, match):
        self.screen.clear()

        match.print_title()
        print("")
        
        print("-" * self.screen.width)
        print("")

    def innings_header(self, innings):        
        print("Innings of " + innings.batting_team.name)
        if innings.bowling_team.score.innings_completed == True:
            print("Target: " + str(innings.bowling_team.score.runs) + " from " + str(innings.overs) + " overs (" + str(round(innings.bowling_team.score.runs / innings.overs, 2)) + " r/o)")
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
        self.header(innings.match)
        self.innings_header(innings)
        print("Innings score: " + str(innings.batting_team.score.runs) + " / " + str(innings.batting_team.score.wickets) + " (" + str(innings.current_over_number) + "." + str(innings.current_ball_number) + " overs)")
        print("")
        if innings.bowling_team.score.innings_completed == True:
            input("Press enter to end the match...")
        else:
            input("Press enter to start the second innings...")

    def results(self, first_innings, second_innings):
        self.header(first_innings.match)
        if first_innings.batting_team.score.runs > second_innings.batting_team.score.runs:
            print(first_innings.batting_team.name + " beat " + second_innings.batting_team.name)
            self.team_scores(first_innings.batting_team, second_innings.batting_team)

        if first_innings.batting_team.score.runs < second_innings.batting_team.score.runs:
            print(second_innings.batting_team.name + " beat " + first_innings.batting_team.name)
            self.team_scores(second_innings.batting_team, first_innings.batting_team)

        if first_innings.batting_team.score.runs == second_innings.batting_team.score.runs:
            print(first_innings.batting_team.name + " vs " + second_innings.batting_team.name + " was a tie!")
            self.team_scores(first_innings.batting_team, second_innings.batting_team)

        print("")
        print("Thank you for playing. Press any key to exit the game.")

    def team_scores(self, first_team, second_team):
        print("")
        first_team.print_name()
        first_team.score.print_score()
        first_team.score.print_total_overs()
        print("")
        second_team.print_name()
        second_team.score.print_score()
        second_team.score.print_total_overs()


    def update(self, innings):
        self.header(innings.match)
        self.innings_header(innings)
        
        print(str(innings.batting_team.score.runs) + " / " + str(innings.batting_team.score.wickets) + " (" + str(innings.current_over_number) + "." + str(innings.current_ball_number) + " overs)")
        print("")
        
        print(innings.batter_on_strike.name + " * (" + str(innings.batter_on_strike.batting_stats.runs) + " off " + str(innings.batter_on_strike.batting_stats.balls) + ")")
        print(innings.batter_off_strike.name + " (" + str(innings.batter_off_strike.batting_stats.runs) + " off " + str(innings.batter_off_strike.batting_stats.balls) + ")")
        print("")

        print("Over " + str(innings.current_over_number + 1))
        print("Bowler: " + innings.bowler.name)
        print(innings.current_over.get_over_stats())
        print("")


