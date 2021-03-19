import gym
from agent import Agent

env = gym.make('Breakout-v0')
agent = Agent()
total_runs = 100

for run in range(total_runs):
    env.reset()
    done = False
    while not done:
        env.render()
        action = agent.sample(env)
        observation, reward, done, info = env.step(action)
        agent.learn(observation, reward)
env.close()
