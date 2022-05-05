print('Setting up...')

import seaborn
import matplotlib.pyplot as plt
import random
import sys
from multiprocessing import Process

trace = bool(input('Do you want to trace trajectories? (Enter to skip)\n'))
number_of_games = int(input('Number of games:\n'))
number_of_steps = int(input('Number of steps:\n'))


result = tuple()

for i in range(number_of_games):
    steps = (0,)
    values = (0,)
    for j in range(number_of_steps):
        values += (values[-1] + random.choice((-1, 1)),)
        steps += (j, )
    result += (values[-1], )

    if trace:
        ax = seaborn.lineplot(x=steps, y=values, )
    sys.stdout.write(f'\r{int(i / number_of_games * 100)}%')

sys.stdout.write('\r100%')

seaborn.set_theme(style="darkgrid")
if trace:
    ax.set(xlabel='steps', ylabel='value', title='Trajectories')

dist = seaborn.displot(result, binwidth=2)
dist.set(xlabel='value', ylabel='number of hitting', title='Hits Distribution')
D = sum(e*e for e in result) / len(result)
print('\n', 'D =', D)

plt.show()