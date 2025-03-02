import os
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../data')

soundcloud_file = os.path.join(DATA, 'soundcloud_times.txt')
youtube_file = os.path.join(DATA, 'youtube_times.txt')


def inter_arrival_times(filename):
    times = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            try:
                time = float(line.split()[0])
                if time > 0:
                    times.append(time)
            except:
                continue
    return np.array(times)


def plot():
    soundcloud_times = inter_arrival_times(soundcloud_file)
    youtube_times = inter_arrival_times(youtube_file)
    plt.figure(figsize=(10, 6))
    sns.histplot(soundcloud_times, color='orange', bins=20, label='Soundcloud', stat='density')
    sns.histplot(youtube_times, color='red', bins=20, label='Youtube', stat='density')
    plt.xscale('log')
    plt.xlabel('Inter-arrival times (s) in log scaling')
    plt.ylabel('Frequency')
    plt.title('Inter-arrival times of Soundcloud and Youtube packets')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    plot()
