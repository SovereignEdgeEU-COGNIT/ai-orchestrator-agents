from test import test
from model import ActorCritic
import torch
import torch.optim as optim
from contextual_bandit import ContextualBandit
import numpy as np

def train():
    gamma = 0.99
    lr = 0.02
    betas = (0.9, 0.999)
    random_seed = 543
    torch.manual_seed(random_seed)
    e = 0.0001
    nr_actions = 6
    np.random.seed(0)

    bandit = ContextualBandit('data.csv')
    policy = ActorCritic()
    optimizer = optim.Adam(policy.parameters(), lr=lr, betas=betas)
    
    running_reward = 0
    for i_episode in range(0, 500):
        bandit.reset()
        for t in range(200):
            state = bandit.step() 
            #if np.random.rand(1) < e:
            #    action = np.random.randint(nr_actions)
            #else:
            #    action = policy(state)
            action = policy(state)
            reward = bandit.pull_arm(action)
            policy.rewards.append(reward)
            running_reward += reward

        print("Episode %s -> Cumlative Reward: %s" % (i_episode, running_reward))
                    
        running_reward = 0
        optimizer.zero_grad()
        loss = policy.calculateLoss(gamma)
        loss.backward()
        optimizer.step()        
        policy.clearMemory()
        
    bandit.print_recommendations(policy)
    torch.save(policy.state_dict(), './pretrained/model.pth'.format(lr, betas[0], betas[1]))
            
if __name__ == '__main__':
    train()
