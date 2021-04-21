from Scoreboard import Scoreboard
from Innings import Innings

class Match:

    team1 = None
    team2 = None
    overs = None
    scoreboard = None

    def __init__(self, team1, team2, overs):
        self.team1 = team1
        self.team2 = team2
        self.overs = overs
        self.scoreboard = Scoreboard()

    def display_title(self):
        print(self.team1.name + " vs " + self.team2.name)

    def start(self, batting_team_name):
        batting_team = self.get_team(batting_team_name)
        bowling_team = self.get_other_team(batting_team_name)

        # first innings
        first_innings = Innings(self, batting_team, bowling_team, self.overs)
        first_innings.start()

        # second innings
        second_innings = Innings(self, bowling_team, batting_team, self.overs)
        second_innings.start()

    def get_team(self, team_name):
        return [team for team in [self.team1, self.team2] if team.name == team_name][0]

    def get_other_team(self, team_name):
        return [team for team in [self.team1, self.team2] if team.name != team_name][0]


