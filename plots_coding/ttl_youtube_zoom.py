import os
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../data')

youtube_ttl_file = os.path.join(DATA, 'youtube_ttl.txt')
zoom_ttl_file = os.path.join(DATA, 'zoom_ttl.txt')


def extract_ttl(filename):
    ttl = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                ttl.append(int(line.split()[0]))
            except:
                continue
    return np.array(ttl)


youtube_ttl = extract_ttl(youtube_ttl_file)
zoom_ttl = extract_ttl(zoom_ttl_file)

bins = np.arange(1, 256)
youtube_hist, _ = np.histogram(youtube_ttl, bins=bins)
zoom_hist, _ = np.histogram(zoom_ttl, bins=bins)

bar_width = 2
x_ind = np.arange(len(bins) - 1)
plt.figure(figsize=(12, 6))
plt.bar(x_ind - bar_width / 2, youtube_hist, color='red', label='Youtube', width=bar_width)
plt.bar(x_ind + bar_width / 2, zoom_hist, color='blue', label='Zoom', width=bar_width)
plt.xlabel('TTL')
plt.ylabel('Frequency')
plt.title('TTL distribution for Youtube and Zoom')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.1)
plt.show()
