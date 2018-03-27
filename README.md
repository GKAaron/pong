# pong
Pong is a game released in 1972. More information could be found on Wikipedia.
This program created a simple version of Pong and used Q-learning to train an agent to play the game.\
First define the Markov Decision Process (MDP):\
State:\
  A tuple (ball_x, ball_y, velocity_x, velocity_y, paddle_y).\
  ball_x and ball_y are real numbers on the interval [0,1]. The lines x=0, y=0, and y=1 are walls; the ball bounces off a wall whenever it hits. The line x=1 is defended by your paddle.\
  The absolute value of velocity_x is at least 0.03, guaranteeing that the ball is moving either left or right at a reasonable speed.\
  paddle_y represents the top of the paddle and is on the interval [0, 1 - paddle_height], where paddle_height = 0.2, as can be seen in the image above. 
Actions: Agent's actions are chosen from the set {nothing, paddle_y += 0.04, paddle_y -= 0.04}. 
In other words, Agent can either move the paddle up, down, or make it stay in the same place. 
If the agent tries to move the paddle too high, so that the top goes off the screen, simply assign paddle_y = 0.
Likewise, if the agent tries to move any part of the paddle off the bottom of the screen, assign paddle_y = 1 - paddle_height.\
Rewards: +1 when action results in rebounding the ball with your paddle, -1 when the ball has passed your agent's paddle, or 0 otherwise.\
Initial State: Use (0.5, 0.5, 0.03, 0.01, 0.5 - paddle_height / 2) as initial state (see the state representation above). 
This represents the ball starting in the center and moving towards your agent in a downward trajectory, 
where the agent's paddle starts in the middle of the screen.\
Here is how discretizes the continuous environment:\
Treat the entire board as a 12x12 grid, and let two states be considered the same if the ball lies within the same cell in this table. Therefore there are 144 possible ball locations.
Discretize the X-velocity of the ball to have only two possible values: +1 or -1 (the exact value does not matter, only the sign).
Discretize the Y-velocity of the ball to have only three possible values: +1, 0, or -1. It should map to Zero if |velocity_y| < 0.015.
Finally, to convert your paddle's location into a discrete value, use the following equation: discrete_paddle = floor(12 * paddle_y / (1 - paddle_height)). In cases where paddle_y = 1 - paddle_height, set discrete_paddle = 11. As can be seen, this discrete paddle location can take on 12 possible values.
Add one special state for all cases when the ball has passed your paddle (ball_x > 1). This special state needn't differentiate among any of the other variables listed above, i.e., as long as ball_x > 1, the game will always be in this state, regardless of the ball's velocity or the paddle's location. This is the only state with a reward of -1.
Therefore, the total size of the state space for this problem is (144)(2)(3)(12)+1 = 10369.
