import numpy as np
import csv

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class ContextualBandit():
    def __init__(self, filename):
        self.data = {} 
        self.row = 0
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                self.data[line_count] = row 
                line_count = line_count + 1

    def step(self):
        self.sunny = float(self.data[self.row]["sunny"])
        self.burger = int(self.data[self.row]["burger"])
        self.extra = int(self.data[self.row]["extra"])

        if self.burger==0:
            state = torch.Tensor([[self.sunny, 1.0, 0, 0, 0, 0]])
        elif self.burger==1:
            state = torch.Tensor([[self.sunny, 0, 1.0, 0, 0, 0]])
        elif self.burger==2:
            state = torch.Tensor([[self.sunny, 0, 0, 1.0, 0, 0]])
        elif self.burger==3:
            state = torch.Tensor([[self.sunny, 0, 0, 0, 1.0, 0]])
        elif self.burger==4:
            state = torch.Tensor([[self.sunny, 0, 0, 0, 0, 1.0]])

        self.row = self.row + 1
        if self.row > len(self.data):
            return None

        return state 
       
    def pull_arm(self,action):
        reward = -1.0 
        if action == self.extra:
            reward = 1.0

        return reward

    def reset(self):
        self.row = 0 

    def print_recommendations(self, policy):
        print()
        print("----------------------------------")
        print("Learned recommendations:")
        print("----------------------------------")
        
        state = torch.Tensor([[0.0, 1.0, 0, 0, 0, 0]])
        action = policy(state)
        print("cloudy: delifresh_burger: ", self.convert_action_to_str(action))

        state = torch.Tensor([[0.0, 0.0, 1.0, 0, 0, 0]])
        action = policy(state)
        print("cloudy: cheese_n_beacon: ", self.convert_action_to_str(action))

        state = torch.Tensor([[0.0, 0.0, 0, 1.0, 0, 0]])
        action = policy(state)
        print("cloudy: salad_warp: ", self.convert_action_to_str(action))

        state = torch.Tensor([[0.0, 0.0, 0, 0, 1.0, 0]])
        action = policy(state)
        print("cloudy: fish_meal: ", self.convert_action_to_str(action))

        state = torch.Tensor([[0.0, 0.0, 0, 0, 0, 1.0]])
        action = policy(state)
        print("cloudy: original_meal: ", self.convert_action_to_str(action))
        
        print()
        
        state = torch.Tensor([[1.0, 1.0, 0, 0, 0, 0]])
        action = policy(state)
        print("sunny: delifresh_burger: ", self.convert_action_to_str(action))

        state = torch.Tensor([[1.0, 0.0, 1.0, 0, 0, 0]])
        action = policy(state)
        print("sunny: cheese_n_beacon: ", self.convert_action_to_str(action))
        
        state = torch.Tensor([[1.0, 0.0, 0, 1.0, 0, 0]])
        action = policy(state)
        print("sunny: salad_warp: ", self.convert_action_to_str(action))
        
        state = torch.Tensor([[1.0, 0.0, 0, 0, 1.0, 0]])
        action = policy(state)
        print("sunny: fish_meal: ", self.convert_action_to_str(action))
        
        state = torch.Tensor([[1.0, 0.0, 0, 0, 0, 1.0]])
        action = policy(state)
        print("sunny: original_meal: ", self.convert_action_to_str(action))

    def convert_action_to_str(self, action):
        if action==0:
            return 'hot_creole'
        if action==1:
            return 'max_original'
        if action==2:
            return 'green_and_carlic'
        if action==3:
            return 'bean'
        if action==4:
            return 'ice_cream'

