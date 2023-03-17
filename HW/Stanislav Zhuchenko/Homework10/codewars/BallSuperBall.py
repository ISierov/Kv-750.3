class Ball:

    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


print(Ball().ball_type)
print(Ball('super').ball_type)
