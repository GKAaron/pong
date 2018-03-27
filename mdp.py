import random
import math


class Paddle:
    def __init__(self):
        self.hight = 0.2
        self.paddle_x = 1
        self.paddle_y = (0.5 - self.hight/2)

    def reset(self):
        self.paddle_y = (0.5 - self.hight/2)

    def move_up(self):
        self.paddle_y += 0.04
        if self.paddle_y + self.hight > 1:
            self.paddle_y = 0

    def move_down(self):
        self.paddle_y -= 0.04
        if self.paddle_y < 0:
            self.paddle_y = 1 - self.hight

    def not_move(self):
        self.paddle_y += 0


class Ball:
    def __init__(self):
        self.ball_x = 0.5
        self.ball_y = 0.5
        self.v_x = 0.03
        self.v_y = 0.01

    def reset(self):
        self.ball_x = 0.5
        self.ball_y = 0.5
        self.v_x = 0.03
        self.v_y = 0.01

    def move(self, paddle:Paddle):
        self.ball_x += self.v_x
        self.ball_y += self.v_y
        if self.ball_y >= 1:
            self.ball_y = 2 - self.ball_y
            self.v_y = - self.v_y
        if self.ball_y <= 0:
            self.ball_y = - self.ball_y
            self.v_y = - self.v_y
        if self.ball_x <= 0:
            self.ball_x = - self.ball_x
            self.v_x = - self.v_x
        if self.ball_x >= 1:
            if paddle.paddle_y <= self.ball_y <= paddle.paddle_y + 0.2:
                self.ball_x = 2 * paddle.paddle_x - self.ball_x
                c = True
                while c:
                    u = random.uniform(-0.015,0.015)
                    v = random.uniform(-0.03,0.03)
                    if math.fabs(u - self.v_x) <= 0.03:
                        continue
                    if math.fabs(u - self.v_x) >= 1:
                        continue
                    if math.fabs(v + self.v_y) >= 1:
                        continue
                    c = False
                self.v_x = u - self.v_x
                self.v_y = v + self.v_y
                return True
        return False



