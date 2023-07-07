import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

def coin_gamble():
    tosses = 0
    while random.randint(0, 1) == 0:
        tosses += 1
    return tosses


if __name__ == '__main__':
    games = []
    for x in tqdm(range(1000000)):
        games.append(coin_gamble()**2)
    print(f"Average: {sum(games) / len(games)}")
    print(f"Max: {max(games)}")
    print(f"Min: {min(games)}")
    print(f"Total: {sum(games)}")
    print(f"Total games: {len(games)}")
    plt.hist([item for item in games if item < 50], bins=100)
    plt.show()
    print(np.unique(games, return_counts=True))


