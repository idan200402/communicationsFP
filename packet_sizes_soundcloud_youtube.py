import os
import numpy as np
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../data')

def packet_sizes(filename):
    path  = os.path.join(DATA, filename)
    sizes = []
    with open (path , 'r') as f:
        for line in f:
            try:
                size = int(line.split()[0])
                sizes.append(size)
            except:
                continue
    return np.array(sizes)


youtube_sizes = packet_sizes('soundcloud_sizes.txt')
soundcloud_sizes = packet_sizes('youtube_sizes.txt')
sorted_youtube_sizes = np.sort(youtube_sizes)
sorted_soundcloud_sizes = np.sort(soundcloud_sizes)

youtube_cdf = np.arange(1 , len(sorted_youtube_sizes)+1) / len(sorted_youtube_sizes)
soundcloud_cdf = np.arange(1 , len(sorted_soundcloud_sizes)+1) / len(sorted_soundcloud_sizes)

plt.figure(figsize=(10, 6))
plt.plot(sorted_youtube_sizes, youtube_cdf, color='red', label='Youtube' )
plt.plot(sorted_soundcloud_sizes, soundcloud_cdf, color='orange', label='Soundcloud' )
plt.xlabel('Packet sizes in bytes')
plt.ylabel('CDF')
plt.title('CDF of Soundcloud and Youtube packet sizes')
plt.legend()
plt.grid(True)
plt.show()