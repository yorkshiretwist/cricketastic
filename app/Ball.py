from Randomiser import Randomiser

class Ball:

    ball_number = None
    result = None
    runs = 0
    dismissal_type = None
    batters_swapped = False
    randomiser = None

    def __init__(self, ball_number, result=None, dismissal_type=None):

        self.randomiser = Randomiser()
        self.ball_number = ball_number

        if result == None:
            self.result = self.get_result()

        if dismissal_type == None and self.result == "W":
            self.dismissal_type = self.get_dismissal_type()

    def get_result(self):

        result = self.randomiser.get_ball_result()
        if result == "1":
            self.batters_swapped = True

        if result.isnumeric():
            self.runs = int(result)

        return result

    def get_dismissal_type(self):

        return self.randomiser.get_dismissal_type()