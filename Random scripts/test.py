import random
from tqdm import tqdm

if __name__ == '__main__':
    sums = []
    avgs = []
    for x in tqdm(range(100)):
        rnd_list = []
        for i in tqdm(range(1000)):
            rnd_list.append(random.randint(1, 6))
        sums.append(sum(rnd_list))
        avgs.append(sum(rnd_list) / len(rnd_list))
    for x in range(100):
        print(f"This is pass: {x}")
        print(sums[x])
        print(avgs[x])

