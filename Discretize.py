from mdp import Ball,Paddle
import math
Size = 15
Velocity = 0.015


def discrete_ball(ball:Ball):
    if ball.ball_x >= 1:
        if ball.v_x > 0:
            co_x = Size
        else:
            co_x = Size - 1
    else:
        co_x = int(ball.ball_x * Size)
    co_y = int(ball.ball_y * Size)
    if co_y == Size:
        co_y -= 1
    if ball.v_x > 0:
        v_x = 1
    else:
        v_x = -1
    if ball.v_y > Velocity:
        v_y = 1
    elif ball.v_y < -Velocity:
        v_y = -1
    else:
        v_y = 0
    return co_x,co_y,v_x,v_y


def discrete_paddle(paddle:Paddle):
    y = int(Size * paddle.paddle_y / (1 - paddle.hight))
    if y == Size:
        y -= 1
    return y


def discrete(ball:Ball,paddle:Paddle)->tuple:
    state = list()
    ball_loc = discrete_ball(ball)
    state.extend(ball_loc[0:2])
    if ball_loc[2] < 0:
        state.append(0)
    else:
        state.append(1)
    if ball_loc[3] < 0:
        state.append(0)
    elif ball_loc[3] == 0:
        state.append(1)
    else:
        state.append(2)
    state.append(discrete_paddle(paddle))
    return tuple(state)







