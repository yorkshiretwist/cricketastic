from Match import Match
from Team import Team
from Interrogator import Interrogator
from Randomiser import Randomiser
from Screen import Screen

class Cricketastic:

    interrogator = None
    randomiser = None
    screen = None
    dev = False

    def __init__(self):
        self.interrogator = Interrogator
        self.randomiser = Randomiser
        self.screen = Screen()

    def run(self):

        if self.dev == False:
            self.screen.display_splash_page()

            team1_name = self.interrogator.get_text("Enter the name for team 1", "The name must be at least 1 character long")
            team2_name = self.interrogator.get_text("Enter the name for team 2", "The name must be at least 1 character long")
            gender = self.interrogator.get_answer("Is this a mens (M), womens (W) or mixed (X) game?", ["M","W","X"], "Please enter a valid choice")
            overs = self.interrogator.get_answer("And how many overs in an innings? (20, 30, 50)", ["2", "20","30","50"], "Please enter a valid choice")
        else:
            team1_name = "Team 1"
            team2_name = "Team 2"
            gender = "X"
            overs = "20"
        
        self.screen.clear()

        team1 = Team(team1_name, gender)
        team2 = Team(team2_name, gender)

        match = Match(team1, team2, int(overs))
        match.display_title()

        print("")
        print("Squads:")
        print("")

        print(team1.name + ":")
        team1.display_squad()
        print("")

        print(team2.name + ":")
        team2.display_squad()
        print("")

        input("Ready to play? Press enter to toss up")
        print("")

        batting_team_name = self.randomiser.get_random_choice([team1.name, team2.name])
        print(batting_team_name + " have elected to bat first.")
        print("")
        input("Press enter to start the match")
        self.screen.clear()

        match.start(batting_team_name)

if __name__ == "__main__":
    cricketastic = Cricketastic()
    cricketastic.run()