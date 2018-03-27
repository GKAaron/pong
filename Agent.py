import Discretize
import numpy as np
import random


class Agent:
    def __init__(self,alpha,exploration,discount=1):
        self.pre_move = None
        self.pre_state = None
        self.pre_reward = None
        self.q_value = np.zeros((Discretize.Size,Discretize.Size,2,3,Discretize.Size,3),dtype='float64')
        self.q_num = np.zeros((Discretize.Size,Discretize.Size,2,3,Discretize.Size,3),dtype='int32')
        self.discount = discount
        self.alpha = alpha
        self.exploration = exploration

    def reset(self):
        self.pre_reward  = None
        self.pre_state = None
        self.pre_reward = None

    def learning_rate(self,num):
        return self.alpha/(self.alpha-1+num)

    def max_q(self,state):
        current_q = self.q_value[state]
        current_num = self.q_num[state]
        act = list()
        for c in range(len(current_num)):
            if current_num[c] < self.exploration:
                return 5,c
        #         act.append(c)
        # if act:
        #     c = act[random.randint(0,len(act)-1)]
        #     return current_q[c],c
        return current_q.max(),current_q.argmax()

    def max_ql(self,state):
        current_q = self.q_value[state]
        return current_q.argmax()

    @staticmethod
    def get_index(state:tuple,act):
        index = list()
        index.extend(state)
        index.append(act)
        return tuple(index)

    def training_acton(self,state:tuple,reward):
        if state == self.pre_state:
            return self.pre_move
        if state[0] == Discretize.Size:
            pre_index = Agent.get_index(self.pre_state, self.pre_move)
            self.q_num[pre_index] += 1
            num = self.q_num[pre_index]
            self.q_value[pre_index] = self.q_value[pre_index] +  self.learning_rate(num)*\
            (self.pre_reward + self.discount*reward - self.q_value[pre_index])
            act = 1 # not move
        elif self.pre_state:
            pre_index = Agent.get_index(self.pre_state, self.pre_move)
            self.q_num[pre_index] += 1
            num = self.q_num[pre_index]
            q_max,act = self.max_q(state)
            self.q_value[pre_index] = self.q_value[pre_index] + self.learning_rate(num)*\
            (self.pre_reward + self.discount*q_max -self.q_value[pre_index])
        else:
            q_max,act = self.max_q(state)
        self.pre_reward = reward
        self.pre_state = state
        self.pre_move = act
        return act

    def action(self,state):
        if state[0] == Discretize.Size:
            return 1
        act = self.max_ql(state)
        return act



