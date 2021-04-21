from Ball import Ball

class Over:

    over_number = None
    balls = []

    def __init__(self, over_number):
        self.balls = []
        self.over_number = over_number

    def get_ball(self, ball_number):

        ball = Ball(ball_number)
        self.balls.append(ball)
        return ball

    def get_over_stats(self):

        results = [ball.result for ball in self.balls]
        return " ".join(results)