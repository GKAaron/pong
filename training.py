import mdp
import Agent
import Discretize
import pickle


ball = mdp.Ball()
paddle = mdp.Paddle()
state = Discretize.discrete(ball,paddle)
agent = Agent.Agent(30,10,0.9)
total_count = 0
all_count= list()
all = list()
for i in range(int(1e5)):
    count = 0
    reward = 0
    while state:
        act = agent.training_acton(state,reward)
        if state[0] != Discretize.Size:
            if act == 0:
                paddle.move_up()
            elif act == 1:
                paddle.not_move()
            else:
                paddle.move_down()
            bounce = ball.move(paddle)
            if bounce:
                reward = 1
                count += 1
            else:
                reward = 0
            state = Discretize.discrete(ball,paddle)
            if state[0] == Discretize.Size:
                reward = -1
        else:
            state = None
    total_count += count
    all_count.append(count)
    if i> 200:
        last_hundred = all_count[-100:-1]
    if i>0 and i%10000 == 0:
        av = sum(last_hundred)/len(last_hundred)
        all.append(av)
    paddle.reset()
    ball.reset()
    agent.reset()
    state = Discretize.discrete(ball,paddle)
av = sum(last_hundred)/len(last_hundred)
f1 = open('agent.txt','wb')
pickle.dump(agent,f1)
f1.close()
print(total_count/0.3e5,av)
