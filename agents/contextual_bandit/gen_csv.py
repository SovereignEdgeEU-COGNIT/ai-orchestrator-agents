import numpy as np
import csv

# states
delifresh_burger = 0 
cheese_n_beacon = 1
salad_warp = 2
fish_meal = 3
original_meal = 4

# actions 
hot_creole = 0
max_original = 1
green_and_carlic = 2
bean = 3
ice_cream = 4

def order_food():
    # states
    sunny = np.random.choice([0, 1], p=[0.8, 0.2]) # sun never shines, like Lulea
    burger = np.random.choice([0, 1, 2, 3, 4], p=[0.2, 0.2, 0.1, 0.1, 0.4])
    
    # when sun shines, everyone want to have ice cream

    if burger == delifresh_burger:
        if sunny == 1:
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.05, 0.05, 0.05, 0.05, 0.8])
        else:
            # bean is most popular
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.09, 0.1, 0.1, 0.7, 0.01])
    elif burger == cheese_n_beacon:
        if sunny == 1:
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.05, 0.05, 0.05, 0.05, 0.8])
        else:
            # hot creol is most popular
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.8, 0.05, 0.09, 0.05, 0.01])

    elif burger == salad_warp:
        if sunny == 1:
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.05, 0.05, 0.05, 0.05, 0.8])
        else:
            # green-and-carlic is most popular
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.09, 0.1, 0.7, 0.1, 0.01])
    
    elif burger == fish_meal:
        if sunny == 1:
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.05, 0.05, 0.05, 0.05, 0.8])
        else:
            # green-and-carlic is most popular
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.1, 0.1, 0.6, 0.1, 0.1])
    
    elif burger == original_meal:
        if sunny == 1:
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.05, 0.05, 0.05, 0.05, 0.8])
        else:
            # max_original dressing is most popular
            extra = np.random.choice([0, 1, 2, 3, 4], p=[0.1, 0.7, 0.09, 0.1, 0.01])

    return sunny, burger, extra

nr_orders = 100000
with open('foodorders.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["row", "sunny", "burger", "extra"])
    
    for i in range(nr_orders):
        order = order_food()
        writer.writerow([i, order[0], order[1], order[2]])
