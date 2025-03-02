import os
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../data')
youtube_file = os.path.join(DATA, 'youtube_window.txt')
soundcloud_file = os.path.join(DATA, 'soundcloud_window.txt')


def extract_window_sizes(filename):
    window_sizes = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                size = int(line.split()[0])
                window_sizes.append(size)
            except:
                continue
    return np.array(window_sizes)


youtube_window_sizes = extract_window_sizes(youtube_file)
soundcloud_window_sizes = extract_window_sizes(soundcloud_file)

youtube_time = np.arange(len(youtube_window_sizes))
soundcloud_time = np.arange(len(soundcloud_window_sizes))


def moving_average(data, window_size=10):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


youtube_smoothed = moving_average(youtube_window_sizes)
soundcloud_smoothed = moving_average(soundcloud_window_sizes)
youtube_time = youtube_time[:len(youtube_smoothed)]
soundcloud_time = soundcloud_time[:len(soundcloud_smoothed)]

plt.figure(figsize=(12, 6))
plt.plot(youtube_time, youtube_smoothed, color='red', label='Youtube', linewidth=2 , alpha=0.7)
plt.plot(soundcloud_time, soundcloud_smoothed, color='orange', label='Soundcloud', linewidth=2 , alpha=0.7)
plt.xlabel('Time (arbitrary units)')
plt.ylabel('Window sizes in bytes')
plt.title('Window sizes of Youtube and SoundCloud packets over time')
plt.legend()
plt.grid(True)
plt.show()
