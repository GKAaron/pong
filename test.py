import pickle
import Agent
import mdp
import Discretize


ball = mdp.Ball()
paddle = mdp.Paddle()
state = Discretize.discrete(ball,paddle)
f1 = open('agent.txt','rb')
agent = pickle.load(f1)
f1.close()
total_count = 0
all = list()
for i in range(1000):
    count = 0
    while state:
        act = agent.action(state)
        if state[0] != Discretize.Size:
            if act == 0:
                paddle.move_up()
            elif act == 1:
                paddle.not_move()
            else:
                paddle.move_down()
            bounce = ball.move(paddle)
            if bounce:
                count += 1
            state = Discretize.discrete(ball, paddle)
        else:
            state = None
    total_count += count
    all.append(count)
    paddle.reset()
    ball.reset()
    agent.reset()
    state = Discretize.discrete(ball,paddle)
av = total_count/1000
print(av)