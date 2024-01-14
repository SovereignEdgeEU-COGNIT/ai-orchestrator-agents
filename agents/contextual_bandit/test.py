from model import ActorCritic
import torch
import torch.optim as optim
from contextual_bandit import ContextualBandit
import numpy as np

def test(n_episodes=10000, name='model2.pth'):
    random_seed = 543
    torch.manual_seed(random_seed)
    np.random.seed(0)

    bandit = ContextualBandit('foodorders.csv')
    policy = ActorCritic()
    policy.load_state_dict(torch.load('./pretrained/{}'.format(name)))

    total_correct = 0
    running_reward = 0
    for i_episode in range(1, n_episodes+1):
        state = bandit.step() 
        action = policy(state)
        reward = bandit.pull_arm(action)
        policy.rewards.append(reward)
        running_reward += reward
        if reward == 1.0:
            total_correct += 1

        print("Sample %s -> Cumlative Reward: %s" % (i_episode, running_reward))

    print()
    print("Total correct:", total_correct)
    print("Precision:", (total_correct/n_episodes))

if __name__ == '__main__':
    test()
