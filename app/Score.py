class Score:
    runs = 0
    wickets = 0
    total_overs = ""
    innings_completed = False

    def print_score(self):
        print(str(self.runs) + " for " + str(self.wickets) + " wickets")

    def print_total_overs(self):
        print("(off " + self.total_overs + " overs)")
